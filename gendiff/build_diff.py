def build_diff(file1, file2):
    keys = sorted(set(file1) | set(file2))
    diff = {}
    for key in keys:
        if key in file1 and key not in file2:
            diff[key] = {'type': 'removed', 'value': file1[key]}
        elif key in file2 and key not in file1:
            diff[key] = {'type': 'added', 'value': file2[key]}
        elif file1[key] == file2[key]:
            diff[key] = {'type': 'unchanged', 'value': file1[key]}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            nested_diff = build_diff(file1[key], file2[key])
            diff[key] = {'type': 'nested', 'value': nested_diff}
        else:
            diff[key] = {
                'type': 'changed',
                'old_value': file1[key],
                'new_value': file2[key]
            }
    return diff
