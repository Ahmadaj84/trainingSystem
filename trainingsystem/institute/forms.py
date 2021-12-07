from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,IntegerField
from wtforms.validators import DataRequired


class InstituteForm(FlaskForm):

    """ Add new institute in the database form linked to the file newinst.html"""

    instName = StringField('إسم المنشأة',validators=[DataRequired(message='يجيب إدخال إسم للمنشأة')])
    supName = SelectField('إسم المشرف' ,validators=[DataRequired(message='يجيب إدخال إسم المشرف')])
    studenMaxNum = IntegerField('عدد الطلاب المسموح' , validators=[DataRequired(message='يجيب تحديد عدد الطلاب المسموح بتدريبهم')])
    submit = SubmitField('Add Institute')
