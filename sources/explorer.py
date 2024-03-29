import os
import subprocess


class Explorer:
    base_path = ""

    def open(self, rel_path: str):
        clean_path = self.clean_path(rel_path)
        abs_path = self.base_path + "\\" + clean_path

        if not self.is_file_inside_base_directory(abs_path):
            raise ValueError("The path provided is not in {}"
                             .format(self.base_path))

        subprocess.Popen(r'explorer /select,"{0}"'.format(abs_path))

    def clean_path(self, file_path: str):
        malicious_chars = ['<', '>', ':', '"', '|', '?', '*', '\n']
        safe_characters = ['_', '_', '_', '_', '_', '_', '_', '']
        new_path = file_path

        for i in range(len(malicious_chars)):
            new_path = new_path.replace(malicious_chars[i], safe_characters[i])

        return new_path

    def is_file_inside_base_directory(self, file_path: str):
        file_abs = os.path.abspath(file_path)

        base_abs = os.path.abspath(self.base_path)

        return os.path.commonpath([file_abs, base_abs]) == base_abs

    def __init__(self, base: str):
        self.base_path = base
