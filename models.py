#Use a form to add the rest of my projects atache files and submmit them POST

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    description = db.Column('Description', db.Text())
    skills_practiced = db.Column('Skills Practiced', db.Text())
    github_link = db.Column('Github Link', db.String())
    main_app = db.Column('Main App', db.Text())
    extra_file01 = db.Column('Extra File 01', db.Text())
    extra_file02 = db.Column('Extra File 02', db.Text())
    extra_file03 = db.Column('Extra File 03', db.Text())

    def __repr__(self):
        return f'''< Project (Title: {self.title}
        Description: {self.description}
        Skills Practiced: {self.skills_practiced}
        Github Link: {self.github_link}
        Main App: {self.main_app}
        Extra File 01: {self.extra_file01}
        Extra File 02: {self.extra_file02}
        Extra File 03: {self.extra_file03})'''



class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Name', db.String())

    def __repr__(self):
        return f'''< Portfolio (Name: {self.name})'''






