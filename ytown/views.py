from ytown import app


@app.route('/')

@app.route('/index')
def index():
    return 'Hello World! From Y-town.'
