import os

from app import app
from app.preprocessing.helpers import (
    get_json_from_saved_excel,
    get_labels_from_json,
    get_values_from_json,
    get_legends_from_json
)

from flask import (
    render_template,
    request
)


@app.route('/display/`')
@app.route('/display/<record_file>/')
def display(record_file):
    # xls_path = os.path.join('/static/', record_file)
    # content_json_list = get_json_from_saved_excel(xls_path)
    # labels = get_labels_from_json(content_json_list)
    # values = get_values_from_json(content_json_list)
    # legends = get_legends_from_json(content_json_list)
    # print('==========================')
    # print(labels, '\n\n', values, '\n\n', legends)
    # return render_template('display.html',
    #                         labels=labels,
    #                         values=values,
    #                         legends=legends)
    return render_template('display.html')
