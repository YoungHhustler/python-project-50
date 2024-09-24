from gendiff.path import read
from gendiff.build_diff import build_diff
from gendiff.formater.stylish import get_stylish
from gendiff.formater.plane import get_plane
from gendiff.formater.json import get_json
from gendiff.pars import parsing


def generate_diff(first_file, second_file, format="stylish"):
    data1, extension = read(first_file)
    data2, extension = read(second_file)
    paresed_data_1 = parsing(data1, extension)
    parsed_data_2 = parsing(data2, extension)
    diff = build_diff(paresed_data_1, parsed_data_2)
    if format == 'stylish':
        return get_stylish(diff)
    elif format == 'plane':
        return get_plane(diff)
    elif format == 'json':
        return get_json(diff)
