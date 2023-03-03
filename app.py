from flask import Flask, request, render_template, redirect, session
import psycopg2
from models.models import login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "87fc31be7c09459324b4801e446098d2";

if __name__ == "__main__":
    app.run(debug = True)

@app.route('/')
def index():
    if session.get('username'):
        return render_template('home.html', username = session.get('username'))
    else:
        return render_template('home.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/my-stats')
def stats():
    return render_template('stats.html')

@app.route('/play-round')
def play():
    return render_template('play.html')


@app.get('/login')
def render_login_page():
    return render_template('login_form.html')

@app.post('/login')
def login():
    username = request.form.get('username')
    print(f"{username} HERE HERE HERE")
    result = login_user(username); 
    print(result)
    if result is None:
        return redirect('/login')
    else:
        session['username'] = result[1]
        return redirect ('/')