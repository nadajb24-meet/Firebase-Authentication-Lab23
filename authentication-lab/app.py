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
  'measurementId': "G-FQZP546P9R", 'databaseURL':'https://nadaaaa-95bef-default-rtdb.firebaseio.com'};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()




@app.route('/', methods=['GET', 'POST'])
def signin():
    error=''
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        try:
            login_session['user']=auth.sign_in_with_email_and_password(email, password)
            return redirect (url_for('add_tweet'))
        except:
            error='Authentication failed'
            return render_template('signin.html')
    else:
        return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=''
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        full_name=request.form['full_name']
        username=request.form['username']
        bio=request.form['bio']
        try:
            login_session['user']=auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user={'email':email,'password':password,'full_name':fullname,'username':username,'bio':bio}
            db.child('users').child(UID).set(user)
            return redirect (url_for('signin'))
        except:
            error='Authentication failed'
            return render_template('signup.html')
    else:
        return render_template('signup.html')


@app.route('/logout')
def logout():
    login_session['user'] =None
    auth.current_user=None
    return redirect (url_for('signup'))



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    error=''
    if request.method=='POST':

        title=request.form['title']
        text=request.form['text']
        try:
            uid=login_session['user']['localId']
            tweet={'title':title,'text':text}
            db.child('tweets').push(tweet)
            return redirect(url_for('all_tweets'))
        except:
            error='ERROR'
    return render_template('add_tweet.html', error=error)

@app.route('/all_tweets')
def all_tweets():
    tweets=db.child('tweets').get().val()
    return render_template('all_tweets.html',tweets=tweets)





if __name__ == '__main__':
    app.run(debug=True)