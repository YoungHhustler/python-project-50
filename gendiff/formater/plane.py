def make_format(value):
    def build(current_value, depth, replacer=' '):
        if not isinstance(current_value, dict):
            return str(value.low())
        indent = replacer * depth
