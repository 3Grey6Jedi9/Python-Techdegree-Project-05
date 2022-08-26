from flask import render_template, url_for, request

from models import db, Portfolio, app





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/new')
def new():
    return "NEW CAT"

@app.route('/projects/<id>')
def detail():
    return "DETAILS"

@app.route('/projects/<id>/edit')
def edit():
    return "EDIT YOUR CAT"

@app.route('/projects/<id>/delete')
def delete():
    return "DELETE YOUR CAT"



#def add_project():
    #n_projects = input('How many projects do you want to add to the database?')
    #while n_projects <=#Now i have to create a function that ask me for my project's data apps included so import files
    #ask for extra files number and apply a while loop 3 while < 3 get extra_file01, extra_file02.... create those columns
    #so doing that I'll get all the porjects into my database and I can start workiong on my website






if __name__ == '__main__':
    #db.create_all()
    #add_project()
    #app.run(debug=True, port=8000, host='127.0.0.1')

    file = open('Projects/old_app.py', 'a')
    filer = open('/Users/danielmulatarancon1/Desktop/TECHDEGREE Projects/Python-Techdegree-Project-04/app.py')
    for row in filer:
        file.write(row)
        break



    # Read and write in a new file that I will save in the database main_app
    #Store in the database then delete the file in order to use it again
    #erase or delete file and create again


