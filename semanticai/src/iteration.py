import json
import subprocess
from src.utils.spinner import Spinner
from src.utils.get_unittest_results import get_unittest_results
from src.utils.strip_path import strip_unittest_path


class Iteration:
    test_summary = {
        "test_response": "",
        "success_count": 0,
        "failure_count": 0,
        "failed_names": [],
        "total_count": 0,
    }

    def __init__(self, prompt, unnittest_path):
        self.prompt = prompt
        self.unnittest_path = unnittest_path
        self.test_summary = Iteration.test_summary
        self.model_response = {}

    def get_success(self, test_output):
        return "OK" in test_output
    
    def generate_completion(self, model, model_name):
        spinner = Spinner(context=f"Computing with {model_name}", delay=0.1)

        with spinner:
            response = model.get_completion(prompt=self.prompt)

        self.model_response = json.loads(response)
        self.write_code_to_file()
        self.run_tests()
        print(f"\nTest summary: {self.test_summary["success_count"]} of {self.test_summary["total_count"]} tests passed\n")

    def write_code_to_file(self):
        test_name, test_path = strip_unittest_path(self.unnittest_path)
        with open(f"{test_path+test_name}.py", "w") as file:
            file.write(self.model_response["code"])

    def run_tests(self):
        test_module_path = self.unnittest_path.replace("/",".").strip(".py")
        command = ["python3", "-m", "unittest", test_module_path]
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.set_test_results(output.stderr)

    def set_test_results(self, test_output):
        test_summary = get_unittest_results(test_output)
        test_summary["test_response"] = test_output
        self.test_summary = test_summary
        
    def create_log_entry(self):
        return {
            "prompt": self.prompt,
            "model_response": self.model_response,
            "tests_summary": self.test_summary,
        }