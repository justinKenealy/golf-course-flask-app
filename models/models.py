from database import sql_select

def login_user(username):
    info = sql_select("SELECT * FROM users WHERE username = %s;", [username])[0]
    return info