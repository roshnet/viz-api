
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

names = []
def get_names(marks_in_json):
    global names
    with open(marks_in_json) as json_file:
        data = json.load(json_file)
        for items in data:
            names.append(items['Name'])
        return names
