from flask import render_template, url_for, flash, redirect, request, Blueprint ,make_response
import pdfkit
from flask_login import login_user, current_user, logout_user, login_required
from trainingsystem import db, bcrypt,main
from trainingsystem.models import User,Institute,Register
from trainingsystem.users.forms import RegistrationForm, LoginForm ,RegistrationForm ,StudintUpdate,StudintChoise


users = Blueprint('users', __name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)#.decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route("/userUpdate" , methods=['GET','POST'])
@login_required
def userUpdate():
    form = StudintUpdate()
    institute = Institute.query.filter_by(available=0)
    section = [(0,'علوم حاسب'),(1,'تقنية المعلومات') , (2,'نظم معلومات') ]
    form.section.choices = section
    if form.validate_on_submit():
        current_user.section =  form.section.data
        current_user.passHours = form.passHours.data
        current_user.gpa = form.gpa.data
        db.session.commit()
        return redirect(url_for('users.studentChoice'))
    else:

        form.gpa.data = current_user.gpa if current_user.gpa != None else 0
        form.passHours.data = current_user.passHours if current_user.passHours != None else 0
        return render_template('userUpdate.html',  form = form)

@users.route("/studentChoice" , methods=['GET','POST'])
@login_required
def studentChoice():
        form = StudintChoise()
        institute = Institute.query.filter_by(available=0)
        form.option1.choices = form.option2.choices = form.option3.choices = [(row.id,row.instName) for row in institute ]

        if form.validate_on_submit():
            current_user.option1 = form.option1.data
            current_user.option2 = form.option2.data
            current_user.option3 = form.option3.data
            register = Register(user_id = current_user.id , sem_id = 1 ,inst_id = current_user.option1 )
            db.session.add(register)
            db.session.commit()

            return redirect(url_for('main.about'))
        else:

            return render_template('studentChoice.html',  form = form)

@users.route("/students" , methods=['GET','POST'])
@login_required
def students():
    if current_user.type == 0 :
        users = User.query.filter_by(type=1)
        return render_template('students.html',title = 'قائمة الطلاب المتقدمين'  , users = users)
    else:
        return redirect(url_for('main.about'))


@users.route("/letter" , methods=['GET'])
@login_required
def letter():
    users = User.query.filter_by(type=1)
    html = render_template('letter.html' )
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response
