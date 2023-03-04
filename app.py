from flask import Flask, request, render_template, redirect, session
import psycopg2
from models.models import login_user, get_course_list, get_course_info, create_new_user
from password_generator import password_generator

app = Flask(__name__)
app.config['SECRET_KEY'] = "87fc31be7c09459324b4801e446098d2";

if __name__ == "__main__":
    app.run(debug = True)

#homepage
@app.route('/')
def index():
    if session.get('username'):
        return render_template('home.html', username = session.get('username'))
    else:
        return render_template('home.html')

#adding new users
@app.route('/signup')
def new_user():
    return render_template('new_user.html')

@app.post('/new_user')
def user_added():
    create_new_user(
        request.form.get('name'),
        request.form.get('username'),
        password_generator(request.form.get('password'))
    )
    return redirect('/login')

#user login 
@app.route('/login')
def render_login_page():
    return render_template('login_form.html')

@app.post('/login')
def login():
    username = request.form.get('username')


    # VALIDATE PASSWORDS HERE AS WELL


    result = login_user(username); 
    if result is None:
        return redirect('/login')
    else:
        session['username'] = result[1]
        return redirect ('/')

#user logout
@app.post('/logout')
def logout_user():
    if session.get('username'):
        session.pop('username')
    return render_template('home.html')


#courses page
@app.route('/courses')
def courses():
    course_list = get_course_list()
    return render_template('courses.html', course_list = course_list)

@app.post('/courses')
def course_selected():
    selected_course_id = request.form.get('courses')
    course_info = get_course_info(selected_course_id)[0]
    print(course_info)
    course_list = get_course_list()
    return render_template('courses.html', course_list = course_list, course_info=course_info)

#play round page
@app.route('/play-round')
def play():
    return render_template('play.html')

