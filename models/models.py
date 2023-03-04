from database import sql_select, sql_select_no_params, sql_write

def login_user(username):
    info = sql_select("SELECT * FROM users WHERE username = %s;", [username])[0]
    return info

def create_new_user(name, username, password_hash):
    sql_write(
        'INSERT INTO users(name, username, password_hash, admin) VALUES (%s, %s, %s, %s);',
        [name, username, password_hash, False])
    return        

def get_course_list():
    info = sql_select_no_params("SELECT id, name FROM courses")
    return info

def get_course_info(id):
    info = sql_select("SELECT * FROM courses WHERE id = %s;", [id])
    return info

def get_course_reviews(course_id):
    info = sql_select("SELECT review_text, rating, username FROM reviews JOIN users ON user_id = users.id WHERE course_id = %s;", [course_id])
    return info
