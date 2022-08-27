from flask import render_template, url_for, request

from models import db, Portfolio, app, Project

import os





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



def get_file(path):
    string = ''
    file = open(path)
    for row in file:
        string += row
    return string



# MANAGE ERRORS


def add_project():
    n_projects = int(input('How many projects do you want to add to the database? '))
    i = 0
    while i < n_projects:
        title = input('Enter the title of the project please: ')
        description = input('Enter a brief description of your project: ')
        skills_practiced = input('Would you be so kind to tell me which skills did you practice? ')
        github_link = input('Now I will need to enter the Github link associated to your project: ')
        path = input('Now I will need the path of the main app of your project: ')
        main_app = get_file(path)
        i += 1
        extra_files = input('How many extra files are associated with the project? ')
        extra_file01 = ''
        extra_file02 = ''
        extra_file03 = ''
        j = 0
        while j < extra_files:
            path = input('Tell me the path of this new extra file please: ')
            if j == 0:
                extra_file01 = get_file(path)
                j += 1
            elif j == 1:
                extra_file02 = get_file(path)
                j += 1
            elif j == 2:
                extra_file03 = get_file(path)
                j += 1
            else:
                print('I am sorry the app it is not configurated for that many extra files. Changes will have to be made')

        new_project = Project(title=title, description=description, skills_practiced=skills_practiced,
                              github_link=github_link, main_app=main_app, extra_file01=extra_file01,
                              extra_file02=extra_file02, extra_file03=extra_file03)
        db.session.add(new_project)
    print('ok we are donde let is commit the data')
    db.session.commit()



    #ask for extra files number and apply a while loop 3 while < 3 get extra_file01, extra_file02.... create those columns
    #so doing that I'll get all the porjects into my database and I can start workiong on my website






if __name__ == '__main__':
    db.create_all()
    add_project()
    #app.run(debug=True, port=8000, host='127.0.0.1')


    #for p in Project.query:
        #print(p)






#FUNCTION TO ADD FILES

    #file = open('Projects/old_app.txt', 'a')
    #filer = open('/Users/danielmulatarancon1/Desktop/TECHDEGREE Projects/Python-Techdegree-Project-04/app.py')
    #for row in filer:
        #file.write(row)
        #break
    #os.remove('Projects/old_app.txt')

    #string = ''
    #filerr = open('/Users/danielmulatarancon1/Desktop/TECHDEGREE Projects/Python-Techdegree-Project-04/app.py')
    #for row in filerr:
        #string += row

    #print(string)
    #print(type(string))

    #This is goint to be how  I will access the data and store in as TEXT into the database





    # Read and write in a new file that I will save in the database main_app
    #Store in the database then delete the file in order to use it again
    #erase or delete file and create again


