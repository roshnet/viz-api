from app import app


@app.route('/join/')
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('index.html')
    return 'You sent POST'
    