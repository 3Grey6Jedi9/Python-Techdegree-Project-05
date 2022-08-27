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
    while ValueError:
        try:
            n_projects = int(input('How many projects do you want to add to the database? '))
        except ValueError:
            print('Please enter an integer')
        else:
            i = 0
            while i < n_projects:
                title = input(f'Enter the title of the project nº{i+1} please: ')
                description = input('Enter a brief description of your project: ')
                skills_practiced = input('Would you be so kind to tell me which skills did you practice? ')
                while ValueError:
                    try:
                        github_link = input('Enter the Github link associated to your project: ')
                        if 'https://github.com/' not in github_link or 'https' != github_link[:5]:
                            raise ValueError('\nI do not think that is a Github link, please try again\n')
                    except ValueError as err:
                        print(f'\n{err}\n')
                    else:
                        break
                while FileNotFoundError:
                    path = input('Enter the path of the main app of your project: ')
                    try:
                        main_app = get_file(path)
                    except FileNotFoundError:
                        print('\nPlease enter a valid path, the file could not be found\n')
                    else:
                        break
                i += 1
                extra_files = int(input('How many extra files are associated with the project? '))
                extra_file01 = ''
                extra_file02 = ''
                extra_file03 = ''
                j = 0
                while j < extra_files:
                    path = input(f'Tell me the path of this new extra nº{j+1} file please: ')
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
            break
    print('Ok we are done, let is commit the data!')
    commit = input("Are you sure do you want to commit the new changes (Enter 'No' to cancel)? " ).lower()
    if commit != 'no':
        db.session.commit()
    else:
        exit()









if __name__ == '__main__':
    db.create_all()
    add_project()
    #app.run(debug=True, port=8000, host='127.0.0.1')


    #for p in Project.query:
        #print(p)

