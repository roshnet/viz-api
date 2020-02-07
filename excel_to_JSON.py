from excel2json import convert_from_file
import os,json

EXCEL_FILE = 'marks.xlsx'
convert_from_file(EXCEL_FILE)
marks_in_json = EXCEL_FILE.split('.')[0] +'.json'
os.rename('Sheet1.json', marks_in_json)

def get_list_from_json(marks_in_json):
    with open(marks_in_json) as json_file:
        data = json.load(json_file)
        return data

list_from_json = get_list_from_json(marks_in_json)
print(list_from_json)
