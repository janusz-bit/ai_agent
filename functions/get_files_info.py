import os


def get_files_info(working_directory, directory="."):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
        valid_target_dir = os.path.commonpath([target_dir, working_directory_abs])
        # print(f"valid_target_dir = {valid_target_dir}")
        if valid_target_dir != working_directory_abs:
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isfile(target_dir):
            return f'Error: "{directory}" is not a directory'

        files = str()
        for thing in os.listdir(target_dir):
            thing_path = os.path.join(target_dir, thing)
            files = (
                files
                + f"- {thing}: file_size={os.path.getsize(thing_path)} bytes, is_dir={os.path.isdir(thing_path)}\n"
            )
        return files

    except Exception as e:
        return f"Error: {e.__str__}"
