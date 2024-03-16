def print_console(text):
    """
    Print the given text to the console.

    Args:
        text (str): The text to print.
    """
    print(text)


def write_file(file_path, content):
    """
    Write the given text to a file.

    Args:
        file_path (str): The path to the file.
        content (str): The content to write to the file.
    """
    with open(file_path, "w") as file:
        file.write(content)
