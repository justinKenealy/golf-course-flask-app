from flask import Flask, request, render_template, redirect, session
import psycopg2
from models.models import get_usernames, remove_rounds_with_course, remove_reviews_with_course, remove_course_from_db, add_request, get_all_requests, edit_course, get_rounds, get_three_rounds, get_five_rounds, get_ten_rounds, submit_scores, login_user, get_course_list, get_course_info, create_new_user, get_course_reviews, add_review_to_db, add_new_course, remove_review_from_db
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
        stats = get_rounds(session.get('user_id'))
        three_rounds = get_three_rounds(session.get('user_id'))
        five_rounds = get_five_rounds(session.get('user_id'))
        ten_rounds = get_ten_rounds(session.get('user_id'))
        total_score_three = 0
        total_putts_three = 0
        total_score_five = 0
        total_score_ten = 0
        total_putts_five = 0
        total_putts_ten = 0
        for round in three_rounds:
            total_score_three += round[0]
            total_putts_three += round[1]
        for round in five_rounds:
            total_score_five += round[0]
            total_putts_five += round[1]
        for round in ten_rounds:
            total_score_ten += round[0]
            total_putts_ten += round[1]
        if len(five_rounds) > 0:
            ave_score_three = "{:.1f}".format(total_score_three/len(three_rounds))
            ave_putts_three = "{:.1f}".format(total_putts_three/len(three_rounds))
            ave_score_five = "{:.1f}".format(total_score_five/len(five_rounds))
            ave_putts_five = "{:.1f}".format(total_putts_five/len(five_rounds))
            ave_score_ten = "{:.1f}".format(total_score_ten/len(ten_rounds))
            ave_putts_ten = "{:.1f}".format(total_putts_ten/len(ten_rounds))
        else:
            ave_score_five = 0
            ave_putts_five = 0
            ave_score_ten = 0
            ave_putts_ten = 0
            stats = 0
        return render_template('home.html', username = session.get('username'), stats = stats, ave_putts_three=ave_putts_three, ave_score_three=ave_score_three, ave_putts_five=ave_putts_five, ave_score_five=ave_score_five, ave_score_ten=ave_score_ten, ave_putts_ten=ave_putts_ten)
    else:
        return render_template('home.html')

#adding new users
@app.route('/signup')
def new_user():
    return render_template('new_user.html')

@app.post('/new_user')
def user_added():
    #add logic so new user can't take existing username
    usernames = get_usernames()
    for string in usernames:
        if request.form.get('username') == string[0]:
            username_error = True
            return render_template('new_user.html', username_error=username_error)

    if request.form.get('password') == request.form.get('password_confirm'):
        create_new_user(
            request.form.get('name'),
            request.form.get('username'),
            password_generator(request.form.get('password'))
        )
        return redirect('/login')
    else:
        password_error = True
        return render_template('new_user.html', password_error=password_error)

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
        if result[4]:
            session['admin'] = True
        return redirect ('/')
    else:
        incorrect = True
        return render_template('login_form.html', incorrect = incorrect)

#user logout
@app.post('/logout')
def logout_user():
    if session.get('username'):
        session.clear()
    return render_template('home.html')


@app.route('/courses')
def course_render(): 
    if session.get('course_id') and session.get('user_id'):
        course_list = get_course_list()
        selected_course_id = session.get('course_id')
        course_info = get_course_info(selected_course_id)[0]
        reviews = get_course_reviews(course_info[0])
        user_id = session.get('user_id')
        reviewed = False
        for review in reviews:
            if review[3] == session.get('user_id'):
                reviewed = True 
        return render_template('courses.html', session_course_id = session['course_id'], selected_course_id = selected_course_id, user_id = user_id, course_list = course_list, course_info=course_info, reviews=reviews, reviewed = reviewed)
    elif session.get('course_id'):
        course_list = get_course_list()
        selected_course_id = session['course_id']
        course_info = get_course_info(selected_course_id)[0]
        reviews = get_course_reviews(course_info[0])
        return render_template('courses.html', session_course_id = session['course_id'], selected_course_id = selected_course_id, course_list = course_list, course_info=course_info, reviews=reviews)
    elif session.get('user_id'):
        course_list = get_course_list()
        user_id = session['user_id']
        return render_template('courses.html', user_id = user_id, course_list = course_list)
    else:
        course_list = get_course_list()
        return render_template('courses.html', course_list = course_list)

@app.post('/courses')
def course_selected():
    selected_course_id = request.form.get('courses')
    session['course_id'] = selected_course_id
    print(selected_course_id)
    course_info = get_course_info(selected_course_id)[0]
    course_list = get_course_list()
    reviews = get_course_reviews(course_info[0])
    if session.get('user_id'):
        user_id = session['user_id']
    else:
        user_id = None
    reviewed = False
    for review in reviews:
        if review[3] == session.get('user_id'):
            reviewed = True 
    return render_template('courses.html', session_course_id = session['course_id'], selected_course_id = selected_course_id, user_id = user_id, course_list = course_list, course_info=course_info, reviews=reviews, reviewed = reviewed)

@app.post('/leave-review')
def leave_review():
  
    add_review_to_db(
        request.form.get('review'), 
        request.form.get('rating'), 
        request.form.get('user_id'),
        request.form.get('course_id')
        )

    return redirect('/courses')

@app.get('/delete-review/<id>')
def remove_review(id):
    remove_review_from_db(id, session['course_id'])
    return redirect('/courses')

#play round page
@app.route('/play-round')
def play():
    course_list = get_course_list()
    return render_template('play.html', course_list = course_list)

@app.post('/play-round')
def submit_round():    
    submit_scores(
        session.get('user_id'),
        request.form.get('course'),
        request.form.get('numShots'),
        request.form.get('numPutts'),
        request.form.get('date')
    )
    return redirect('/')

#add course
@app.route('/add-course')
def add_course():
    if session.get('admin'):
        return render_template('add_course.html')
    else:
        return redirect('/')

@app.post('/add-course')
def course_added():
    add_new_course(
        request.form.get('name'),
        request.form.get('link'),
        request.form.get('description'),
        request.form.get('par'),
        request.form.get('logo'),
        request.form.get('image')    
    )
    return redirect('/courses')

@app.route('/requests')
def requests():
    course_requests = get_all_requests()
    print(course_requests)
    return render_template('requests.html', course_requests = course_requests)

@app.post('/request')
def add_request_form():
    add_request(
        request.form.get('course_name'),
        request.form.get('course_link')
    )
    return redirect('/play-round')

@app.route('/request-course')
def new_request():
    return render_template('new_request.html')

#edit course
@app.route('/edit')
def edit_page():
    print(session.get('course_id'))
    info = get_course_info(session.get('course_id'))[0]
    return render_template('edit_course.html', info=info)

@app.post('/edited-course')
def edited_course():
    edit_course(
        request.form.get('name'),
        request.form.get('description'),
        request.form.get('par'),
        request.form.get('logo'),
        request.form.get('image'),
        request.form.get('link'),
        session.get('course_id')
    )
    return redirect('/courses')

#remove course & rounds & reviews
@app.route('/remove-course')
def remove_course():
    remove_rounds_with_course(session.get('course_id'))
    remove_reviews_with_course(session.get('course_id'))
    remove_course_from_db(session.get('course_id'))
    session.pop('course_id')
    return redirect('/courses')
