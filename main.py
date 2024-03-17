from app.io.output import print_console, write_file
from app.io.input import read_console, read_file_builtin, read_file_pandas


def main():
    user_input = read_console()

    # reading user input and writing it to data/console_input.txt
    print_console(user_input)
    write_file("data/console_input.txt", user_input)

    # reading data from data/console_input.txt using built-in file reading and writing it to the console
    file_lines = read_file_builtin("data/console_input.txt")
    if file_lines is None:
        print_console("The file does not exist.")
    else:
        print_console("\n".join(file_lines))

    # reading data from data/pandas_input.csv using pandas and writing it to the console and data/pandas_output.txt
    pandas_file = read_file_pandas("data/pandas_input.csv")
    if pandas_file is None:
        print_console("The file does not exist.")
    else:
        print_console(pandas_file.to_string())
        write_file("data/pandas_output.txt", pandas_file.to_string())


if __name__ == "__main__":
    main()
