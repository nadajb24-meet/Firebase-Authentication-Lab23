from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config  = {
  'apiKey': "AIzaSyAr1b5rBX1lB1gd26qjKukkkiG83GrO2AQ",
  'authDomain': "nadaaaa-95bef.firebaseapp.com",
  'projectId': "nadaaaa-95bef",
  'storageBucket': "nadaaaa-95bef.appspot.com",
  'messagingSenderId': "166283185570",
  'appId': "1:166283185570:web:9363106071dee8928176fb",
  'measurementId': "G-FQZP546P9R", 'databaseURL':''
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()




@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)