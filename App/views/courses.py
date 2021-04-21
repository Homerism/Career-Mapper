from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory, flash, url_for
from flask_login import current_user, login_required
from wtforms import Form, SelectMultipleField
courses_views = Blueprint('courses_views', __name__, template_folder='../templates')
from App.controllers import(get_courses_json, get_courses, get_jobs)
from App.models import Courses, Jobs, db
from App.forms import CourseForm


#<----------------Course Form------------------------>
@courses_views.route('/courses', methods=['GET'])
@login_required
def courses():
    form = CourseForm()
    courses = Courses.query.all()
    jobs = Jobs.query.all()
    return render_template('courses.html', form=form, courses=courses, jobs=jobs)

@courses_views.route("/courses", methods=["GET", "POST"])
@login_required
def courseAction():
     form = CourseForm() # create form object
     if form.validate_on_submit():
        data = request.form # get data from form submission
        choices = request.form.getlist('jobchoices') #This is the name of the checkboxes
        newcourse = Courses(courseName=data['coursename'], courseDescription=data['coursedescription'], skills=data['skills']) # create course object 
        db.session.add(newcourse) # save new course
        db.session.commit()
        flash('Course Created!')# send message
        return redirect(url_for('courses_views.courses'))# redirect to the dashboard page
        flash('Error invalid input!')
        return redirect(url_for('courses_views.courses')) 

#<-------------------Delete Course----------------------->

@courses_views.route('/deleteCourse/<courseID>', methods=['GET'])
@login_required
def delete_course(courseID):
    course = Courses.query.filter_by(courseID=courseID).first() # query course (Once models fix add user ID)
    if course:
        db.session.delete(course)
        db.session.commit()
        flash('Course Deleted!')
        return redirect(url_for('courses_views.courses'))
    flash('Unauthorized or course not found')
    return redirect(url_for('courses_views.courses'))


@courses_views.route('/selectCourse/<courseID>', methods=['GET'])
def course_jobs(courseID):
    courses = Courses.query.filter_by(courseID=courseID).first() # query course (Once models fix add user ID)
    return render_template('courseJobs.html', course=course)