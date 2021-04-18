from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime

class Jobs(db.Model):
    jobID = db.Column(db.Integer, primary_key=True)
    jobName = db.Column(db.String(80), nullable=False)
    jobDescription = db.Column(db.String(1000), nullable=False)
    requirements = db.Column(db.String(1000), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.courseID'), nullable=False)
    def toDict(self):
        return {
            "jobID": self.jobID,
            "jobName": self.jobName,
            "jobDescription": self.jobDescription,
            "requirements": self.requirements
            }