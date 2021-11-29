from datetime import datetime
from TrainingSystem import db, login_manager
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
    student = db.Column(db.Integer, default=1)#is the user student with value 1 and the value 0 means admin or doctor
    section = db.Column(db.String(60))#قسم الطالب
    passHours = db.Column(db.Numeric)#الساعات المجتازة
    gpa = db.Column(db.Numeric)
    mobile = db.Column(db.String(10))
    inst_id = db.Column(db.Integer, db.ForeignKey('institute.id'), nullable=True)
    institute = db.relationship("Institute",back_populates="users" ) #جهة التدريب
    option1 = db.Column(db.Integer)
    option2 = db.Column(db.Integer)
    option3 = db.Column(db.Integer)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    #posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Institute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instName = db.Column(db.String(200))
    supName = db.Column(db.String(100))
    mobile = db.Column(db.String(10))
    email = db.Column(db.String(120), unique=True, nullable=False)
    studenMaxNum = db.Column(db.Integer)
    users = db.relationship("User",back_populates = "institute")
    #user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=True)

    def __repr__ (self):
        return f"Institute('{self.instName}', '{self.supName}')"


    """
    inst_1 = Institute(instName = 'Ministry of health makkah', supName = 'Ahmad jifry' , mobile = '0000000000' , email = 'mazin@moh.gov.sa')
    inst_2 = Institute(instName = 'Ministry of health Jeddah', supName = 'mazin jifry' , mobile = '0555555555' , email = 'ahmad@moh.gov.sa')
    user_1 = User(username = 'ahmad', email = 'a@demo.com',password='password',passHours='3.5' ,gpa = '4.5' )
    """




""" class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')" """
