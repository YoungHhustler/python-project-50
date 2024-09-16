from gendiff.path import read_files
from gendiff.build_diff import build_diff
from gendiff.formater.stylish import get_stylish
# from gendiff.formater.plane import get_stylish


def generate_diff(first_file, second_file, format='stylish'):
    file1, file2 = read_files(first_file, second_file)
    diff = build_diff(file1, file2)
    formated = get_stylish(diff)
    return print(formated)


generate_diff('gendiff/files/file1_tree.yml', 'gendiff/files/file2_tree.yml')
