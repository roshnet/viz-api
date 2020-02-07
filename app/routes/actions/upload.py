from app import app
from flask import (
    render_template,
    request, redirect
)
import os
from excel2json import convert_from_file


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        excel = request.files.get('excel')
        # BUG: check whether to use '/' or not in upload path.
        save_path = os.path.join('/static/uploads', excel.filename)
        excel.save(save_path)
        convert_from_file(save_path)
        marks_in_json = save_path.split('.')[0] = '.json'
        os.rename('Sheet1.json', marks_in_json)
        return redirect('/display')
    return render_template('upload.html')
