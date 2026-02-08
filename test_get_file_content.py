from functions.get_file_content import get_file_content


def test(function):
    def f(*args):
        return print(function(*args))

    return f


test(get_file_content)("calculator", "main.py")
test(get_file_content)("calculator", "pkg/calculator.py")
test(get_file_content)("calculator", "/bin/cat")  # (this should return an error string)
test(get_file_content)(
    "calculator", "pkg/does_not_exist.py"
)  # (this should return an error string)
