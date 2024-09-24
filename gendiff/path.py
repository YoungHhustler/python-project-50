import os


def read(file_path):
    _, format = os.path.splitext(file_path)
    with open(file_path) as data:
        data = data.read()
        return data, format
