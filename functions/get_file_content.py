import os

from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_file = os.path.commonpath([target_file, working_directory_abs])
        if working_directory_abs != valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        file = open(target_file, mode="r")
        read_data = file.read(MAX_CHARS)
        if file.read(1):
            read_data += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return read_data
    except Exception as e:
        return "Error: " + e.__str__()


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Show content of a file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to read, relative to the working directory",
            ),
        },
    ),
)
