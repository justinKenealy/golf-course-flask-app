INSERT INTO users (name, email, password_hash, admin) VALUES ('Justin', 'justinmkenealy@gmail.com', '', True);

INSERT INTO courses (
    name, 
    web_link, 
    course_description, 
    par_score, 
    logo_image, 
    course_image, 
    course_map, 
    hole_scores) 
    VALUES 
    ('name', 
    'web_link', 
    'course_description', 
    72, 
    'logo_image', 
    'course_image', 
    'course_map', 
    'hole_scores') 

INSERT INTO rounds (user_id, course_id, total_score, total_putts, hole_scores) 
    VALUES (1, 1, 72, 36, '[4,4,4,4,4,4,4,4,4,4,4,4]')