from werkzeug.security import generate_password_hash

def password_generator(password):
    password_hash = generate_password_hash(password)
    return password_hash