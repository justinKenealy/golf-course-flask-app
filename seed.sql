-- TRUNCATE TABLE users CASCADE;
-- TRUNCATE TABLE courses CASCADE;
-- TRUNCATE TABLE rounds CASCADE;

-- ALTER SEQUENCE users_id_seq RESTART WITH 1;
-- ALTER SEQUENCE courses_id_seq RESTART WITH 1;
-- ALTER SEQUENCE rounds_id_seq RESTART WITH 1;

-- INSERT INTO users (name, username, password_hash, admin) VALUES ('Justin', 'justinkenealy', '', True);

-- INSERT INTO courses (
--     name, 
--     web_link, 
--     course_description, 
--     par_score, 
--     logo_image, 
--     course_image, 
--     course_map, 
--     hole_scores) 
--     VALUES 
--     ('Kew Golf Club', 
--     'https://www.kewgolfclub.com.au/', 
--     'Situated only 15 minutes from the city, the course meanders along the Yarra River providing a beautiful vista and is home for more than a hundred species of native birds.', 
--     72, 
--     'data:image/png;base64,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', 
--     'https://www.kewgolfclub.com.au/cms/wp-content/gallery/course/Kew_17AerialFWWide_0993.jpg', 
--     'https://www.kewgolfclub.com.au/cms/wp-content/uploads/2020/10/KewGC-Course-Map-1-1536x1431.jpg', 
--     '[4, 4, 4, 3, 5, 4, 5, 4, 4, 4, 3, 5, 4, 3, 4, 5, 4, 3]');

-- INSERT INTO rounds (user_id, course_id, total_score, total_putts, hole_scores) 
--     VALUES (1, 1, 72, 32, '[4,4,5,4,6,3,5,3,4,4,4,5,4,4,4,5,4,2]');

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
    ('Green Acres Golf Club', 
    'http://www.greenacresgolf.com.au/', 
    'Green Acres Golf Club is Melbourne''s premier Yarra River golf course with a proud history dating back to 1948. Ideally located just moments from the bustling heart of the city in a lush and tranquil riverside setting, Green Acres provides members with exclusive access to a challenging 18-hole course, a contemporary clubhouse, a comprehensive golf centre and a friendly sense of community.',
    72, 
    'http://www.greenacresgolf.com.au/resources/images/logo.jpg',
    'http://www.greenacresgolf.com.au/cms_uploads/images/51_1st-1.jpg',
    '',
    '[4, 4, 5, 3, 3, 4, 4, 5, 3, 4, 3, 4, 4, 5, 4, 4, 3, 4]');

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
    ('Latrobe Golf Club', 
    'https://www.latrobegolf.com.au/', 
    'Latrobe Golf Club is a beautiful course in the leafy suburb of Alphington, just 10 Km from Melbourne''s CBD. It is bordered on two sides by the Yarra River and lined by majestic Red River Gums.',
    72, 
    'https://www.latrobegolf.com.au/cms/wp-content/themes/latrobe/images/logo.png',
    'https://golf-pass.brightspotcdn.com/dims4/default/38567c0/2147483647/strip/true/crop/1440x929+0+14/resize/930x600!/quality/90/?url=https%3A%2F%2Fgolf-pass-brightspot.s3.amazonaws.com%2F1a%2Fb2%2Fd747df0edadbff7ef0b979e46959%2F100014.jpg',
    '',
    '[3, 5, 4, 4, 4, 4, 4, 4, 3, 4, 3, 5, 3, 4, 4, 5, 4, 5]');