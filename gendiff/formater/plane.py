def get_plane(diff, path=''):
    lines = []
    for key, val in diff.items():
        property_path = f"{path}{key}"
        if val['type'] == 'added':
            lines.append(f"Property '{property_path}' "
                         f"was added with value: "
                         f"{str_value(val['value'])}")
        if val['type'] == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        if val['type'] == 'nested':
            nested_value = get_plane(val['value'], f"{property_path}.")
            lines.append(f"{nested_value}")
        if val['type'] == 'changed':
            lines.append(f"Property '{property_path}' was updated. "
                         f"From {str_value(val['old_value'])} to "
                         f"{str_value(val['new_value'])}")
    return '\n'.join(lines)


def str_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    if value is None:
        return "null"
    return f"'{value}'"
