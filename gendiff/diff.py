from gendiff.path import read_files
from gendiff.build_diff import build_diff
from gendiff.formater.stylish import get_stylish
from gendiff.formater.plane import get_plane
from gendiff.formater.json import get_json


def generate_diff(first_file, second_file, format):
    file1, file2 = read_files(first_file, second_file)
    diff = build_diff(file1, file2)
    if format == 'stylish':
        return print(get_stylish(diff))
    elif format == 'plane':
        return print(get_plane(diff))
    elif format == 'json':
        return print(get_json(diff))


# generate_diff('gendiff/files/file1_tree.json', 'gendiff/files/file2_tree.json', 'stylish')
