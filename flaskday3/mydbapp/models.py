from mydbapp.settings import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(20))
    sex = db.Column(db.String(20))


