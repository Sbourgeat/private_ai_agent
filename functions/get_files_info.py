import os


def get_files_info(working_directory: str, directory: str = ".") -> str | None:

    if not os.path.isdir(directory):
        print(f'Error: "{directory}" is not a directory')

    absolute_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(absolute_path, directory))
    valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

    if not valid_target_dir:
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
    else:
        print(f'Success: "{target_dir}" is within the working directory')

        for file in os.listdir(target_dir):
            file_name = file
            file_size = os.path.getsize(os.path.join(target_dir, file))
            is_dir = os.path.isdir(os.path.join(target_dir, file))

            print(f"- {file_name}: file_size={file_size}, is_dir={is_dir}")
