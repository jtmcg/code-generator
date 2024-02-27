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