from flask import render_template, request, Blueprint,url_for,redirect
from flask_login import login_user, current_user, logout_user, login_required


main = Blueprint('main', __name__)

@main.route("/home")
@login_required
def home():
    if current_user.type == 0 :
        return redirect (url_for('users.students'))
    elif current_user.type == 1:
        return redirect(url_for('users.studentChoice'))
    else:
        return render_template('about.html', title='About')

@main.route("/")
@main.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')
