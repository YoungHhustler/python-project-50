def format_to_stylish(value):
    return build(value, 0)


def build(current_value, depth, replacer=" "):
    if not isinstance(current_value, dict):
        return stylish_to_string(current_value)

    indent = replacer * depth
    child_depth = depth + 4
    result = ["{"]

    for key, val in current_value.items():
        string = ""
        if isinstance(val, dict):
            string = build_node(val.get("type"), indent, key, val, child_depth)
            result.extend(string)
        else:
            string = build_string(indent, key, val, child_depth)
            result.append(string)

    result.append(indent + "}")
    return "\n".join(result)


def build_node(type, indent, key, val, depth):
    result = []
    match type:
        case "nested":
            string = f"{indent}    {key}: {build(val['value'], depth)}"
        case "added":
            string = f"{indent}  + {key}: {build(val['value'], depth)}"
        case "removed":
            string = f"{indent}  - {key}: {build(val['value'], depth)}"
        case "unchanged":
            string = f"{indent}    {key}: {build(val['value'], depth)}"
        case "changed":
            string = f"{indent}  - {key}: {build(val['old_value'], depth)}"
            result.append(string)
            string = f"{indent}  + {key}: {build(val['new_value'], depth)}"
        case None:
            string = f"{indent}    {key}: {build(val, depth)}"
        case _:
            raise ValueError("Wrong node type")
    result.append(string)
    return result


def build_string(indent, key, value, child_depth):
    string = f"{indent}    {key}: {build(value, child_depth)}"
    return string


def stylish_to_string(value):
    if value is False:
        return "false"
    elif value is True:
        return "true"
    elif value is None:
        return "null"
    else:
        return f"{str(value)}"
