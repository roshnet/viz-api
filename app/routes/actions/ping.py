from app import app
from flask import (
    render_template,
    request, redirect
)


@app.route('/ping/')
def ping():
    return "OK"