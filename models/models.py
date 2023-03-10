from database import sql_select, sql_select_no_params, sql_write, sql_write_no_params

def login_user(username):
    info = sql_select("SELECT * FROM users WHERE username = %s;", [username])[0]
    return info

def create_new_user(name, username, password_hash):
    sql_write(
        'INSERT INTO users(name, username, password_hash, admin) VALUES (%s, %s, %s, %s);',
        [name, username, password_hash, False]
        )
    return        

def get_course_list():
    info = sql_select_no_params("SELECT id, name FROM courses")
    return info

def get_course_info(id):
    info = sql_select("SELECT * FROM courses WHERE id = %s;", [id])
    return info

def get_course_reviews(course_id):
    info = sql_select("SELECT review_text, rating, username, user_id FROM reviews JOIN users ON user_id = users.id WHERE course_id = %s;", [course_id])
    return info

def add_review_to_db(review_text, rating, user_id, course_id):
    sql_write(
        'INSERT INTO reviews(review_text, rating, user_id, course_id) VALUES (%s, %s, %s, %s);',
        [review_text, rating, user_id, course_id]
    )
    return

def remove_review_from_db(user_id, course_id):
    sql_write('DELETE FROM reviews WHERE user_id = %s AND course_id = %s;', [user_id, course_id])
    return

def add_new_course(name, link, description, par, logo, img):
    sql_write(
        'INSERT INTO courses(name, web_link, course_description, par_score, logo_image, course_image) VALUES (%s, %s, %s, %s, %s, %s);',
        [name, link, description, par, logo, img]
    )
    return

def edit_course(name, description, par_score, logo, image, link, id):
    sql_write(
        'UPDATE courses SET name = %s, course_description = %s, par_score = %s, logo_image = %s, course_image = %s, web_link = %s WHERE id = %s;',
        [name, description, par_score, logo, image, link, id]
    )

def remove_course_from_db(id):
    sql_write(
        'DELETE FROM courses WHERE id = %s', [id]
    )

def remove_rounds_with_course(id):
    sql_write(
        'DELETE FROM rounds WHERE course_id = %s', [id]
    )

def remove_reviews_with_course(id):
    sql_write(
        'DELETE FROM reviews WHERE course_id = %s', [id]
    )

def submit_scores(user_id, course_id, total_score, total_putts, date):
    sql_write(
        'INSERT INTO rounds(user_id, course_id, total_score, total_putts, round_date) VALUES (%s, %s, %s, %s, %s);',
        [user_id, course_id, total_score, total_putts, date]
    )
    return

def get_rounds(user_id):
    info = sql_select(
        'SELECT user_id, course_id, name, par_score, total_score, total_putts, round_date FROM rounds JOIN courses on courses.id = rounds.course_id WHERE user_id = %s ORDER BY round_date DESC', [user_id] 
    )
    return info

def get_three_rounds(user_id):
    info = sql_select(
        'SELECT total_score - par_score AS score, total_putts FROM rounds JOIN courses on courses.id = rounds.course_id WHERE user_id = %s ORDER BY round_date DESC LIMIT 3', [user_id] 
    )
    return info

def get_five_rounds(user_id):
    info = sql_select(
        'SELECT total_score - par_score AS score, total_putts FROM rounds JOIN courses on courses.id = rounds.course_id WHERE user_id = %s ORDER BY round_date DESC LIMIT 5', [user_id] 
    )
    return info

def get_ten_rounds(user_id):
    info = sql_select(
        'SELECT total_score - par_score AS score, total_putts FROM rounds JOIN courses on courses.id = rounds.course_id WHERE user_id = %s ORDER BY round_date DESC LIMIT 10', [user_id] 
    )
    return info

def add_request(course_name, course_link):
    sql_write(
        'INSERT INTO requests(course_name, course_link) VALUES (%s, %s);',
        [course_name, course_link]
    )
    return

def get_all_requests():
    info = sql_select_no_params("SELECT course_name, course_link FROM requests")
    return info

def get_usernames():
    info = sql_select_no_params("SELECT username FROM users")
    return info