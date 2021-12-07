from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from trainingsystem import db
from trainingsystem.models import Institute , User
from trainingsystem.institute.forms import InstituteForm


institutes = Blueprint('institutes', __name__)


@institutes.route("/newinst" , methods=['GET', 'POST'])
@login_required
def newinst():
    form = InstituteForm()
    users = User.query.filter_by(type=2)
    form.supName.choices = [(u.id,u.username) for u in users]
    if form.validate_on_submit():
        institute = Institute(instName = form.instName.data, user_id = form.supName.data,studenMaxNum = form.studenMaxNum.data)
        db.session.add(institute)
        db.session.commit()
        flash('تم إضافة ' + institute.instName, 'success')
        return redirect(url_for('main.about'))
    return render_template('newinst.html',title='New Institute' , form=form)
