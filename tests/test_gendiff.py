from gendiff.diff import generate_diff


FILE1_JSON = 'gendiff/files/file1.json'
FILE2_JSON = 'gendiff/files/file2.json'
FILE1_YAML = 'gendiff/files/file1.yaml'
FILE2_YAML = 'gendiff/files/file2.yaml'


def test_generate_diff_json():
    diff = generate_diff(FILE1_JSON, FILE2_JSON)
    assert diff == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_generate_diff_yaml():
    diff = generate_diff(FILE1_YAML, FILE2_YAML)
    assert diff == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
