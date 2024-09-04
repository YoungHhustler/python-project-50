from gendiff.gendiff import generate_diff
from tests.fixtures import path


def test_generate_diff():
    diff = generate_diff(path.file1, path.file2)
    assert diff == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
