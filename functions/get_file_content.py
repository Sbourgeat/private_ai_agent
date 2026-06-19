import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    absolute_path = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(absolute_path, file_path))
    valid_target_file = os.path.commonpath([absolute_path, target_file]) == absolute_path

    valid_file = os.path.isfile(target_file)
    if not valid_file:
        print(f'Error: File not found or is not a regular file: "{file_path}"')

    if not valid_target_file:
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if valid_target_file and valid_file:
        with open(target_file, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content
