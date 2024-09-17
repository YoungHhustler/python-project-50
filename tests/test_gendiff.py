import pytest
from gendiff.diff import generate_diff


def read_file(filepath):
    with open(filepath) as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, format, expected", [
        ("tests/fixtures/file1_tree.json", "tests/fixtures/file2_tree.json", 'stylish', read_file('tests/fixtures/correct_result_stylish.txt')),
        ("tests/fixtures/file1_tree.json", "tests/fixtures/file2_tree.json", 'plane', read_file('tests/fixtures/correct_result_plane.txt')),
        ("tests/fixtures/file1_tree.json", "tests/fixtures/file2_tree.json", 'json', read_file('tests/fixtures/correct_result_json.txt')),
        ("tests/fixtures/file1_tree.yml", "tests/fixtures/file2_tree.yml", 'stylish', read_file('tests/fixtures/correct_result_stylish.txt')),
        ("tests/fixtures/file1_tree.yml", "tests/fixtures/file2_tree.yml", 'plane', read_file('tests/fixtures/correct_result_plane.txt')),
        ("tests/fixtures/file1_tree.yml", "tests/fixtures/file2_tree.yml", 'json', read_file('tests/fixtures/correct_result_json.txt'))
    ]
)
def test_generate_diff(file1, file2, format, expected):
    assert generate_diff(file1, file2, format) == expected
