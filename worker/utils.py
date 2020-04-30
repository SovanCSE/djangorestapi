import json

def is_vaild_json(json_data):
    try:
        json.loads(json_data)
        is_valid=True
    except ValueError:
        is_valid =False
    return is_valid
