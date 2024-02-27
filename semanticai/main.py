import json
import subprocess
import sys
from src.logger import Logger, LogEntry
from src.spinner import Spinner
from src.completion import GPT
from src.prompts import construct_initial_prompt, construct_iteration_prompt, construct_iterative_success_prompt
from src.utils.strip_path import strip_unittest_path
from src.utils.get_unittest_results import get_unittest_results

def generate_code(unittest_path):

    model = "gpt-4-turbo-preview"
    gpt = GPT(model, temperature=0.5)
    logger = Logger("gpt_responses", "src/logs/logs.json")
    test_summary = {}
    most_successful_run = {
        "code": "",
        "test_results": None,
    }

    test_name, test_path = strip_unittest_path(unittest_path)

    # Open test file
    with open(unittest_path, "r") as file:
        unittest_code = file.read()

    iteration = 0

    def get_success(test_output):
        return "OK" in test_output

    while (True):
        log_entry = LogEntry()
        log_entry.set_tests_string_input(unittest_code)
        print(f"\niteration {iteration}")
        if iteration == 0:
            prompt = construct_initial_prompt("python", unittest_code)
            log_entry.set_prompt(prompt)
        elif test_summary["success_count"] > most_successful_run["test_results"]["success_count"]:
            prompt = construct_iterative_success_prompt(
                json_response["code"], 
                unittest_code, 
                output.stderr, 
                test_summary, 
                test_summary["success_count"] - most_successful_run["test_results"]["success_count"], 
                [failed_name for failed_name in most_successful_run["test_results"]["failed_names"] if failed_name not in test_summary["failed_names"]]
            )
            most_successful_run["code"] = json_response["code"]
            most_successful_run["test_results"] = test_summary
        else:
            prompt = construct_iteration_prompt(json_response["code"], unittest_code, output.stderr, test_summary)
            log_entry.set_prompt(prompt)
            log_entry.set_code_string_input(json_response["code"])
            log_entry.set_test_results(output.stderr)

        spinner = Spinner(context='Computing with LLM', delay=0.1)

        with spinner:
            response = gpt.get_completion(prompt=prompt)

        json_response = json.loads(response)
        log_entry.set_model_response(json_response)

        # output response string to a python file. Need to keep track of how many files we've created
        with open(f"{test_path+test_name}.py", "w") as file:
            file.write(json_response["code"])

        # run tests against the response
        test_module_path = unittest_path.replace("/", ".").strip(".py")
        command = ["python3", "-m", "unittest", test_module_path]
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        log_entry.set_test_results(output.stderr)

        test_summary = get_unittest_results(output.stderr)
        log_entry.set_response_summary(test_summary)

        logger.log(log_entry.create_log_entry())
        if iteration == 0:
            most_successful_run["test_results"] = test_summary
            most_successful_run["code"] = json_response["code"]

        if get_success(output.stderr):
            break

        if "ImportError: Failed to import test module" in output.stderr:
            print(f"Failed to import test module {test_name} from {test_path}")
            break
        iteration += 1
        
        if iteration > 10:
            break
    logger.close_log()
    logger.write_logs_to_file(f"{test_path+test_name}_logs.txt")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <unittest_path>")
        sys.exit(1)
    else: 
        generate_code(sys.argv[1])