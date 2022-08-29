from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    description = db.Column('Description', db.Text())
    skills = db.Column('Skills Practiced', db.Text())
    github = db.Column('Github Link', db.String())
    main_app = db.Column('Main App', db.Text())
    extra_file01 = db.Column('Extra File 01', db.Text())
    extra_file02 = db.Column('Extra File 02', db.Text())
    extra_file03 = db.Column('Extra File 03', db.Text())

    def __repr__(self):
        return f'''< Old_Project (Title: {self.title}
        Created: {self.date}
        Description: {self.description}
        Skills Practiced: {self.skills}
        Github Link: {self.github}
        Main App: {self.main_app}
        Extra File 01: {self.extra_file01}
        Extra File 02: {self.extra_file02}
        Extra File 03: {self.extra_file03})'''









