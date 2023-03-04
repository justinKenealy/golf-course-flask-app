from flask import Flask, request, render_template, redirect, session
import psycopg2
from models.models import login_user, get_course_list, get_course_info, create_new_user, get_course_reviews
from werkzeug.security import generate_password_hash, check_password_hash

def password_generator(password):
    password_hash = generate_password_hash(password)
    return password_hash


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
    #add logic so new user can't take existing username
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
    password = request.form.get('password')
    result = login_user(username); 
    password_matches = check_password_hash(result[3], password)
    if result is not None and password_matches:
        session['username'] = result[1]
        session['user_id'] = result[0]
        print(session['user_id'])
        return redirect ('/')
    else:
        incorrect = True
        return render_template('login_form.html', incorrect = incorrect)

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
    session['course_id'] = course_info[0]
    course_list = get_course_list()
    reviews = get_course_reviews(course_info[0])
    print(reviews)
    return render_template('courses.html', course_list = course_list, course_info=course_info, reviews=reviews)

#play round page
@app.route('/play-round')
def play():
    return render_template('play.html')

