from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField ,DecimalField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from trainingsystem.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('البريد الإلكتروني',
                        validators=[DataRequired(), Email()])
    password = PasswordField('كلمة المرور', validators=[DataRequired()])
    remember = BooleanField('تذكرني')
    submit = SubmitField('تسجيل الدخول')

class StudintUpdate(FlaskForm ):
    """docstring for StudintOption. so that a student can register in three diffrent institute"""
    section =  SelectField('القسم' ,validators=[DataRequired(message= 'يجيب تحديد القسم')])
    passHours = DecimalField('الساعات المنجزة' ,validators=[DataRequired(message= 'يجيب تحديد عدد الساعات')])
    gpa = DecimalField('المعدل التراكمي'  ,validators=[DataRequired(message= 'حدد المعدل التراكمي الحالي')])
    submit = SubmitField('تسجيل')

class StudintChoise(FlaskForm ):
    """docstring for StudintOption. so that a student can register in three diffrent institute"""
    option1 = SelectField('الإختيار الأول'  ,validators=[DataRequired(message= 'يجيب إدخال رغبات جهات التدريب')])
    option2 = SelectField('الإختيار الثاني',validators=[DataRequired(message= 'يجيب إدخال رغبات جهات التدريب')])
    option3 = SelectField('الإختيار الثالث' ,validators=[DataRequired(message= 'يجيب إدخال رغبات جهات التدريب')])
    submit = SubmitField('تسجيل')
