from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField ,DecimalField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from trainingsystem.models import User


class RegistrationForm(FlaskForm):
    username = StringField('إسم المستخدم',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('البريد الإلكتروني',
                        validators=[DataRequired(), Email()])
    password = PasswordField('كلمة السر', validators=[DataRequired()])
    confirm_password = PasswordField('تأكيد كلمة السر',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('تسجيل')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('سبق إستخدام إسم المستخدم هذا , نرجو إختيار إسم آخر')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('سبق إستخدام البريدالإلكتروني هذا!')

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
