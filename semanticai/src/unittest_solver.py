from src.gpt_client import GPT
from src.iteration import Iteration
from src.logger import Logger
from src.prompts import construct_initial_prompt, construct_iteration_prompt, construct_iterative_success_prompt, construct_regression_prompt
from src.utils.strip_path import strip_unittest_path


class UnittestSolver:
    
    def __init__(self, unittest_path, model_name="gpt-3.5-turbo", temperature=0.5):
        self.unittest_path = unittest_path
        self.unittest_code_string = self.get_unittest_code_string(unittest_path)
        self.model_name = model_name
        self.gpt = GPT(model_name, temperature)
        self.most_successful_iteration = None
        self.iterations = []
        unittest_name, _ = strip_unittest_path(unittest_path)
        self.logger = Logger("gpt_responses", f"src/logs/{unittest_name}.json")

    def generate_code(self):

        while (True):
            iteration = Iteration(self.get_prompt(), self.unittest_path)
            iteration.generate_completion(self.gpt, self.model_name)

            self.iterations.append(iteration)
            self.logger.log(iteration.create_log_entry())

            if iteration.test_summary["success_count"] == iteration.test_summary["total_count"]:
                print("\nSuccess!")
                break

            if "ImportError: Failed to import test module" in iteration.test_summary["test_response"]:
                print(f"Failed to import test module from {self.unittest_path}")
                break

            if len(self.iterations) > 10:
                print("Iteration limit reached... Exiting")
                break

        self.logger.close_log()

    def get_unittest_code_string(self, path):
        with open(path) as file:
            return file.read()
        
    def get_prompt(self):
        num_iterations = len(self.iterations)
        if num_iterations == 0:
            print("Generating initial prompt...")
            prompt = construct_initial_prompt("python", self.unittest_code_string)
        elif num_iterations == 1:
            print("Generating prompt for first iteration...")
            self.most_successful_iteration = self.iterations[0]
            prompt = construct_iteration_prompt(
                self.iterations[0].model_response["code"],
                self.unittest_code_string,
                self.iterations[0].test_summary["test_response"],
                self.iterations[0].test_summary,
                )
        elif num_iterations > 1:
            if self.iterations[-1].test_summary["success_count"] > self.most_successful_iteration.test_summary["success_count"]:
                print("Generating prompt for improved iteration...")
                prompt = construct_iterative_success_prompt(
                    self.iterations[-1].model_response["code"],
                    self.unittest_code_string,
                    self.iterations[-1].test_summary["test_response"],
                    self.iterations[-1].test_summary,
                    self.most_successful_iteration.test_summary["success_count"] - self.iterations[-1].test_summary["success_count"],
                    [failed_name for failed_name in self.most_successful_iteration.test_summary["failed_names"] if failed_name not in self.iterations[-1].test_summary["failed_names"]],
                    )
                self.most_successful_iteration = self.iterations[-1]
            elif self.iterations[-1].test_summary["success_count"] < self.most_successful_iteration.test_summary["success_count"]:
                print("Generating prompt for regression...")
                prompt = construct_regression_prompt(
                    self.unittest_code_string,
                    self.iterations[-1].test_summary["test_response"],
                    self.most_successful_iteration.model_response["code"],
                    [failed_name for failed_name in self.iterations[-1].test_summary["failed_names"] if failed_name not in self.most_successful_iteration.test_summary["failed_names"]],
                    )    
            else:
                print("Generating prompt for no progress...")
                prompt = construct_iteration_prompt(
                    self.iterations[-1].model_response["code"],
                    self.unittest_code_string,
                    self.iterations[-1].test_summary["test_response"],
                    self.iterations[-1].test_summary,
                )
        
        return prompt