
def remove_field_from_json(file_path):
    if os.path.exists(file_path):
        with open(file_path) as fp:
            data = json.load(fp)
        for elem in data:
            elem.pop('Name')
        return data
    return 1

def get_name_from_json(file_path):
    """Return only `name` key JSON"""
    if os.path.exists(file_path):
        with open(file_path) as fp:
            data = json.load(fp)


    return 1
