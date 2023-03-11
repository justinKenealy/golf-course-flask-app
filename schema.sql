DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS courses CASCADE;
DROP TABLE IF EXISTS rounds CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    admin BOOL NOT NULL
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    web_link TEXT,
    course_description TEXT,
    par_score INT NOT NULL,
    logo_image TEXT,
    course_image TEXT,
    course_map TEXT,
    hole_scores TEXT,
);

CREATE TABLE rounds (
    id SERIAL PRIMARY KEY,
    user_id INT,
    CONSTRAINT fk_rounds_users
        FOREIGN KEY(user_id)
        REFERENCES users(id),
    course_id INT,
    CONSTRAINT fk_rounds_courses
        FOREIGN KEY(course_id)
        REFERENCES courses(id),
    total_score INT,
    total_putts INT,
    hole_scores TEXT,
    round_date DATE
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    review_text TEXT,
    rating INT NOT NULL, 
    user_id INT,
    CONSTRAINT fk_rounds_users
        FOREIGN KEY(user_id)
        REFERENCES users(id),
    course_id INT,
    CONSTRAINT fk_rounds_courses
        FOREIGN KEY(course_id)
        REFERENCES courses(id)
);

CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    course_name TEXT,
    course_link TEXT
);