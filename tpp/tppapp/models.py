from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Letter(db.Model):
    __tablename__ = 'letter'
    id = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(20),nullable=False)
    cities = db.relationship("City",backref="letter")
class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    regionName = db.Column(db.String(20),nullable=False)
    cityCode = db.Column(db.Integer,nullable=False)
    pinYin = db.Column(db.String(20), nullable=False)
    letter_id = db.Column(db.Integer,db.ForeignKey("letter.id"))
