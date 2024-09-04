from gendiff.path import read_files


def generate_diff(first_file, second_file):
    file1, file2 = read_files(first_file, second_file)
    keys = sorted(set(file1 | file2))
    diff = []
    for key in keys:
        if key in file2 and key not in file1:
            diff.append(f'  + {key}: {file2[key]}')
        elif key in file2 and key in file1 and file1[key] != file2[key]:
            diff.append(f'  - {key}: {file1[key]}')
            diff.append(f'  + {key}: {file2[key]}')
        elif key not in file2:
            diff.append(f'  - {key}: {file1[key]}')
        else:
            diff.append(f'    {key}: {file1[key]}')
    return ("{\n" + "\n".join(diff).lower() + "\n}")
