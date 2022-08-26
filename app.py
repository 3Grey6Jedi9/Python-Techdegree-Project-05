from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Great Cats'

@app.route('/projects/new')
def new():
    return "NEW CAT"

@app.route('/projects/<id>')
def detail():
    return "DETAILS"

@app.route('/projects/<id>/edit')
def edit():
    return:"EDIT YOUR CAT"

@app.route('/projects/<id>/delete')
def delete():
    return "DELETE YOUR CAT"






if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')


