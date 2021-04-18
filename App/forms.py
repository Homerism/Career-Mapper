from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms.fields.html5 import EmailField

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class JobForm(FlaskForm):
    jobname = StringField('Job Name')
    jobdescription = StringField('Job Description')
    requirements = StringField('Requirments')
    submit = SubmitField('SubmitJob')


#class CourseForm(FlaskForm):
    #coursename = StringField('Course Name')
    #coursedescription = StringField('Course Description')
    #skills = StringField('Skills')
    #submit = SubmitField('SubmitCourse')