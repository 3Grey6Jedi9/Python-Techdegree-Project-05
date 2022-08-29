import datetime

from flask import render_template, url_for, request, redirect

from models import db, Old_Project, app, New_Project

import os




def clean_date(strdate):
    datep = datetime.datetime.strptime(strdate, '%Y-%m')
    return datep





@app.route('/')
def index():
    old_projects = Old_Project.query.all()
    new_projects = New_Project.query.all()
    return render_template('index.html', old_projects=old_projects, new_projects=new_projects)




@app.route('/about')
def about():
    return render_template('about.html')





@app.route('/projects/new', methods=['GET', 'POST'])
def new():
    if request.form:
        new_project = New_Project(title=request.form['title'], date=clean_date(request.form['date']),
                                   description=request.form['desc'],
                                   skills=request.form['skills'], github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')




@app.route('/projects/<id>')
def detail(id):
    old_projects = Old_Project.query.all()
    new_projects = New_Project.query.all()
    return render_template('detail.html', old_projects=old_projects, new_projects=new_projects)





@app.route('/projects/<id>/edit')
def edit(id):
    return "EDIT YOUR CAT"





@app.route('/projects/<id>/delete')
def delete(id):
    return "DELETE YOUR CAT"






def get_file(path):
    string = ''
    file = open(path)
    for row in file:
        string += row
    return string




def add_old_project():
        while ValueError:
            try:
                n_projects = int(input('How many old projects do you want to add to the database? '))
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

                    new_project = Old_Project(title=title, description=description, skills_practiced=skills_practiced,
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
    add_old_project()
    app.run(debug=True, port=8000, host='127.0.0.1')



