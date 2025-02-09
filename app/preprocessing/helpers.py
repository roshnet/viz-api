import os
import json


def get_json_from_saved_excel(excel_file_name):
    if os.path.exists(excel_file_name):
        with open(excel_file_name) as fp:
            return json.load(fp)
    return 1


def get_values_from_json(file_path):
    """Return only `name` key JSON"""
    if os.path.exists(file_path):
        with open(file_path) as fp:
            data = json.load(fp)
    return 1


def get_labels_from_json(file_path):
    if os.path.exists(file_path):
        with open(file_path) as fp:
            data = json.load(fp)
        for elem in data:
            elem.pop('Name')
        return data
    return 1


def get_legends_from_json(marks_in_json):
    names = []
    with open(marks_in_json) as json_file:
        data = json.load(json_file)
        for items in data:
            names.append(items['Name'])
        return names


def get_list_from_json(marks_json):
    with open(marks_json) as fp:
        return json.load(fp)
