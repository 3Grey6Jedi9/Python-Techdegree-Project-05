import datetime

from flask import render_template, url_for, request, redirect

from models import db, Project, app






def clean_date(strdate):
    datep = datetime.datetime.strptime(strdate, '%Y-%m')
    return datep





@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)




@app.route('/about')
def about():
    return render_template('about.html')





@app.route('/projects/new', methods=['GET', 'POST'])
def new():
    if request.form:
        new_project = Project(title=request.form['title'], date=clean_date(request.form['date']),
                                   description=request.form['desc'],
                                   skills=request.form['skills'], github=request.form['github'],
                              )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')




@app.route('/projects/<id>')
def detail(id):
    project = Project.query.get(id)
    return render_template('detail.html', project=project)





@app.route('/projects/<id>/edit')
def edit(id):
    return "EDIT YOUR CAT"





@app.route('/projects/<id>/delete')
def delete(id):
    return "DELETE YOUR CAT"









if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')







