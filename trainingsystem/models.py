from datetime import datetime
from trainingsystem import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    uniID = db.Column(db.Integer, unique=True)#الرقم الجامعي
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    type = db.Column(db.Integer, default=1)#is the user student with value 1 and the value 0 means admin , 2 for institute supervisor
    section = db.Column(db.Integer)#قسم الطالب
    passHours = db.Column(db.Numeric)#الساعات المجتازة
    gpa = db.Column(db.Numeric)
    mobile = db.Column(db.String(10))
    #inst_id = db.Column(db.Integer, db.ForeignKey('institute.id'), nullable=True)
    #institute = db.relationship("Institute",back_populates="users" ) #جهة التدريب
    inst = db.relationship('Institute',backref = 'supervisor' , lazy=True)
    option1 = db.Column(db.Integer)
    option2 = db.Column(db.Integer)
    option3 = db.Column(db.Integer)
    student = db.relationship('Register' , backref = 'student', lazy=True)

    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    #posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Institute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instName = db.Column(db.String(200))

    studenMaxNum = db.Column(db.Integer)
    available = db.Column(db.Integer , default=0) #flag once the number of the registered student equal the studenMaxNum it turn to 1
    #users = db.relationship("User",back_populates = "institute")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=True)

    def __repr__ (self):
        return f"Institute('{self.instName}', '{self.supervisor.username}')"

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sem_id = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    def __repr__ (self):
        return f"Register('{self.user_id}', '{self.sem_id}')"


class Semester(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    name = db.Column(db.String(30))
    register = db.relationship("Register" , backref = 'semester', lazy=True)
    def __repr__ (self):
        return f"Semester('{self.year}', '{self.name}')"



"""
    inst_1 = Institute(instName = 'Ministry of health makkah' ,studenMaxNum = 3)
    inst_2 = Institute(instName = 'Ministry of health Jeddah', studenMaxNum = 4)
    user_1 = User(username = 'ahmad', email = 'a@demo.com',password='password',passHours='3.5' ,gpa = '4.5' )
    user_2 = User(username = 'mazin', email = 'mazin@demo.com',password='password',passHours='3.5' ,gpa = '4.5' )
    supervisor = User(username = 'sameer', email = 'sam@demo.com',password='password' )
    sem_1 = Semester(year = 2021 , name='Summer')
    reg = Register(student = user_1 ,semester = sem_1)
"""




""" class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')" """
