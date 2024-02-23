import json
import subprocess
import sys
from src.completion import GPT
from src.prompts import construct_initial_prompt, construct_iteration_prompt
from src.utils import strip_unittest_path

def generate_code(unittest_path):

    model = "gpt-3.5-turbo"
    gpt = GPT(model)

    test_name, test_path = strip_unittest_path(unittest_path)

    # Open test file
    with open(unittest_path, "r") as file:
        unittest_code = file.read()

    iteration = 0

    def get_success(test_output):
        return "OK" in test_output

    while (True):
        print(f"iteration {iteration}")
        if iteration == 0:
            prompt = construct_initial_prompt("python", unittest_code)
        else:
            prompt = construct_iteration_prompt(output.stderr)

        response = gpt.get_completion(prompt=prompt)
        json_response = json.loads(response)

        # output response string to a python file. Need to keep track of how many files we've created
        with open(f"{test_path+test_name}.py", "w") as file:
            file.write(json_response["code"])

        # run tests against the response
        command = ["python3", "-m", "unittest", unittest_path]
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(output)
        if get_success(output.stderr):
            break

        if "ImportError: Failed to import test module" in output.stderr:
            print(f"Failed to import test module {test_name} from {test_path}")
            break
        iteration += 1
        if iteration > 10:
            break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <unittest_path>")
        sys.exit(1)
    else: 
        generate_code(sys.argv[1])