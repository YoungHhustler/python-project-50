import json
import yaml


def read_files(first_file, second_file):
    def read_file(file_path):
        if file_path.endswith('.json'):
            return json.load(open(file_path))
        if file_path.endswith(('.yml', '.yaml')):
            return yaml.safe_load(open(file_path))
    file1 = read_file(first_file)
    file2 = read_file(second_file)
    return file1, file2

# print(read_files('gendiff/files/file1.yml', 'gendiff/files/file2.yml'))
