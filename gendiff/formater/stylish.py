def get_stylish(diff, replacer=" ", spaces_count=4):
    def build(value, depth):
        if not isinstance(value, dict):
            if value is True:
                return "true"
            elif value is False:
                return "false"
            elif value is None:
                return "null"
            return str(value)
        current_indent = replacer * depth
        child_indent_size = depth + spaces_count
        child_indent = replacer * (child_indent_size - 2)
        children = ["{"]
        for key, val in value.items():
            if isinstance(val, dict) and 'type' in val:
                type = val['type']
                if type == 'nested':
                    nested = build(val['value'], child_indent_size)
                    children.append(f'{current_indent}    {key}: {nested}')
                elif type == 'added':
                    added = build(val['value'], child_indent_size)
                    children.append(f'{child_indent}+ {key}: {added}')
                elif type == 'removed':
                    removed = build(val['value'], child_indent_size)
                    children.append(f'{child_indent}- {key}: {removed}')
                elif type == 'unchanged':
                    unchanged = build(val['value'], child_indent_size)
                    children.append(f'{current_indent}    {key}: {unchanged}')
                elif type == 'changed':
                    old_value = build(val['old_value'], child_indent_size)
                    new_value = build(val['new_value'], child_indent_size)
                    children.append(f'{child_indent}- {key}: {old_value}')
                    children.append(f'{child_indent}+ {key}: {new_value}')
            else:
                children.append(f'{current_indent}    {key}: {build(val, child_indent_size)}')
        children.append(current_indent + "}")
        return '\n'.join(children)
    return build(diff, 0)
