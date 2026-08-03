def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    """
    Writes the provided content to a file.
    :param file_path: Path to the file where content will be written.
    :param content: Content to be written to the file.
    """
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path, content):
    """
    Appends the provided content to an existing file.
    :param file_path: Path to the file where content will be appended.
    :param content: Content to be appended to the file.
    """
    with open(file_path, 'a') as file:
        file.write(content)


def read_lines(file_path):
    """
    Reads the content of a file line by line.
    :param file_path: Path to the file to be read.
    :return: List of lines from the file.
    """
    with open(file_path, 'r') as file:
        return file.readlines()


def is_file_exists(file_path):
    """
    Checks if a file exists at the specified path.
    :param file_path: Path to the file.
    :return: True if the file exists, otherwise False.
    """
    import os
    return os.path.isfile(file_path)