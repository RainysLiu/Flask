from migrateapp.settings import *
class Toy(db.Model):
    __tablename__ =  'toy'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Float,nullable=False)




#一对多关联表
class School(db.Model):
    __tablename__ = 'school'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    students = db.relationship("Student",backref="sch")
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10),nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    score = db.Column(db.String(10), nullable=False)
    school_id = db.Column(db.Integer,db.ForeignKey("school.id"))



#一对一关联表

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    #从面向对象角度关联
    card = db.relationship("IDcard",backref = 'per',uselist=False)
class IDcard(db.Model):
    __tablename__ = 'idcard'
    cardid = db.Column(db.String(20),primary_key=True)
    balance = db.Column(db.Integer)
    address = db.Column(db.String(20))
    per_id = db.Column(db.Integer,db.ForeignKey("person.id"),unique=True)



#多对多表关联

middle = db.Table("children_hobby",
                  db.Column("children_id",db.Integer,db.ForeignKey("children.id"),primary_key=True),
                  db.Column("hobby_id",db.Integer,db.ForeignKey("hobby.id"),primary_key=True)
                  )
class Children(db.Model):
    __tablename__ = 'children'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(20))
    hobbies = db.relationship('Hobby',secondary='children_hobby',backref=db.backref('children'))
class Hobby(db.Model):
    __tablename__ = 'hobby'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))




#作业

# 出版社(Publisher)与书(Book)是“一对多”关系，书（Book）与作者(Author)是“多对多”关系

class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    address = db.Column(db.String(20),nullable=False)
    books = db.relationship("Book",backref="pub")
middletable = db.Table(
    'author_book',
     db.Column("author_id",db.Integer,db.ForeignKey("author.id"),primary_key=True),
     db.Column("book_id",db.Integer,db.ForeignKey('book.id'),primary_key=True),
    )
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(20))
    books = db.relationship('Book',secondary="author_book",backref=db.backref("author"))

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10),nullable=False)
    publisher_id = db.Column(db.Integer,db.ForeignKey("publisher.id"))

