# trainingSystem
This project is to register and evaluate student with Co-up training institute using flask environment.

This code is pushed to be published on the website: ahmadaj84.pythonanywhere.com   

To run local host you need to:
copy all files in local directory
navigate using the command line
type if you are using windows "set FLASK_APP=flasking.py"
next type "flask run"
now the local server should be running and you can run this code from the browser  

Runing the db from python
from flaskblog import db
db.create_all() (it will create all the tables )
from flaskblog import User,POST
user_1 = User(username = 'ahmad', email = 'a@demo.com',password='password')
db.session.add(user_1)
user_2 = User(username = 'rozana', email = 'r@demo.com',password='password')
db.session.add(user_2)
db.session.commit()


User.query.all()
