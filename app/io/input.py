import pandas as pd


def read_console():
    """
    Prompt the user to enter some text and return it.

    Returns:
        str: The input entered by the user.
    """
    return input("Enter some text: ")


def read_file_builtin(file_path):
    """
    Read the contents of a file and return it as a string.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        list[str]: The contents of the file as a list of strings.

    Raises:
        RuntimeError: If the file does not exist.
    """
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        raise RuntimeError("File not found")


def read_file_pandas(file_path):
    """
    Read the contents of a file and return it as a pandas DataFrame.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        pd.DataFrame: The contents of the file as a DataFrame.

    Raises:
        RuntimeError: If the file does not exist or is empty.
    """
    try:
        return pd.read_csv(file_path)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        raise RuntimeError("File not found or empty")
