from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    password = db.Column(db.String(20))
    token = db.Column(db.String(20))
    permission = db.Column(db.Integer)

    def has_permission(self,permission):
        return self.permission & permission == permission


