import json

class Logger:
    def __init__(self, name, log_path):
        self.name = name
        self.logs = []
        self.log_path = log_path

    def log(self, message):
        self.logs.append(message)
        if len(self.logs) == 1:
            with open(self.log_path, "w", encoding="utf-8") as file:
                file.write("[")
        elif len(self.logs) > 1:
            with open(self.log_path, "a", encoding="utf-8") as file:
                file.write(",")
            
        with open(self.log_path, "a", encoding="utf-8") as file:
            json.dump(message, file, ensure_ascii=False, indent=4)

    def close_log(self):
        with open(self.log_path, "a", encoding="utf-8") as file:
            file.write("]")

    def write_logs_to_file(self, file_path):
        with open(file_path + ".json", "w", encoding="utf-8") as file:
            json.dump(self.logs, file, ensure_ascii=False, indent=4)

class LogEntry:
    def __init__(self):
        self.prompt = ''
        self.tests_string_input = ''
        self.code_string_input = ''
        self.model_response = ''
        self.test_results = ''

    def set_prompt(self, prompt):
        self.prompt = prompt

    def set_tests_string_input(self, tests_string_input):
        self.tests_string_input = tests_string_input

    def set_code_string_input(self, code_string_input):
        self.code_string_input = code_string_input

    def set_model_response(self, model_response):
        self.model_response = model_response

    def set_test_results(self, test_results):
        self.test_results = test_results

    def create_log_entry(self):
        return {
            "prompt": self.prompt,
            "tests_string_input": self.tests_string_input,
            "code_string_input": self.code_string_input,
            "model_response": self.model_response,
            "test_results": self.test_results
        }