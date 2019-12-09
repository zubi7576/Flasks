from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
myapp = Flask(__name__)

myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
myapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////absolute/path/to/Admin.db'
db = SQLAlchemy(myapp)

class Admin(db.Model):
    id = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=True, nullable=False)
@myapp.route('/user', methods=["POST"])
def mySignup():
    # print(request.form['username'])

    if request.method == "POST":
        admin = Admin()
        admin.name = request.form['name']
        admin.email = request.form['email']
        admin.password = request.form['password']
        db.session.add(admin)
        db.session.commit()
        return  render_template('Profile.html')

@myapp.route('/user')
def user():
    return "<h2>User Added</h2>"


@myapp.route('/')
def SignUp():
    return render_template('SignUp.html')
myapp.run()