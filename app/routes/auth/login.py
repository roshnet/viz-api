from app import app
from flask import (
        request,
        render_template
)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
