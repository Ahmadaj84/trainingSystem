from flask import render_template, request, Blueprint


main = Blueprint('main', __name__)

@main.route("/home")
def home():
    return render_template('about.html', title='About')


@main.route("/")
@main.route("/about")
def about():
    return render_template('about.html', title='About')
