from werkzeug.security import generate_password_hash, check_password_hash

def password_generator(password):
    password_hash = generate_password_hash(password)
    return password_hash

print(password_generator('justin123'))
