import json
import yaml


def parsing(data, format):
    if format == '.json':
        return json.loads(data)
    elif format == '.yaml' or '.yml':
        return yaml.safe_load(data)