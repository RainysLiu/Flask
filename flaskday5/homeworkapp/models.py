


from homeworkapp.settings import db


class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    students = db.relationship("Student",backref="cls")
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10),nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer,nullable=False)
    score = db.Column(db.String(10), nullable=False)
    class_id = db.Column(db.Integer,db.ForeignKey("class.id"))



