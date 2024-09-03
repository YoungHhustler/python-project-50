import json


def generate_diff(first_file, second_file):
    file_1 = json.load(open(first_file))
    file_2 = json.load(open(second_file))
    keys = sorted(set(file_1 | file_2))
    diff = []
    for key in keys:
        if key in file_2 and key not in file_1:
            diff.append(f'  + {key}: {file_2[key]}')
        elif key in file_2 and key in file_1 and file_1[key] != file_2[key]:
            diff.append(f'  - {key}: {file_1[key]}')
            diff.append(f'  + {key}: {file_2[key]}')
        elif key not in file_2:
            diff.append(f'  - {key}: {file_1[key]}')
        else:
            diff.append(f'    {key}: {file_1[key]}')
    return ("{\n" + "\n".join(diff).lower() + "\n}")
