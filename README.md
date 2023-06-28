# Golf Buddy

## Description
Golf Buddy is a full-stack application that allows users to store and track their statistics and view the details of a number of different golf clubs. Users may also review each course, and request that a specific course is added to the database. Only admins may add, edit, and remove courses. Users input the details of their round to add it to their own statistics log, where they can view their scores for their last round, or averages over their last 3, 5, and 10 rounds. User can also view a table of all of their scores which they can then export to an XLS file. 

## Screenshots
<div>
  <img src="./screenshots/golfbuddy1.png" alt="tasker entry page" width="90%" style="display: inline-block; margin: 10px;">
  <img src="./screenshots/golfbuddy2.png" alt="tasker entry page" width="90%" style="display: inline-block; margin: 10px;">
  <img src="./screenshots/golfbuddy3.png" alt="tasker entry page" width="90%" style="display: inline-block; margin: 10px;">
  <img src="./screenshots/golfbuddy4.png" alt="tasker entry page" width="90%" style="display: inline-block; margin: 10px;">
<div>


## Technologies used
### HTML
- All pages are rendered through HTML
- Jinja is used for templating

### CSS
- Multiple CSS files to style the different pages

### Python
- Python FLASK hosts the server, and a combination of ROUTE, GET, POST requests are drawn on by the application

### JavaScript
- JavaScript was used to add interactivity.
- Users interact with buttons to display or hide certain elements on the page
- A function to export to excel file is used on the home page
- A setInterval function is used to render a rotating golf quote/joke

### PostgreSQL
- Data is stored on the backend across five tables: users, courses, requests, reviews and rounds. 
- Password encryption and authentication is used to safely allow user access
- Foreign keys join tables to link the users to their own statistics
- Foreign keys join tables to link the statistics to the relevant course
- Foreign keys join tables to link each review to a user and the relevant course