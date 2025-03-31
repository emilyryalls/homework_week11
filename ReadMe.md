Flask App - Group One

Start:
 * Run app.py to start the Flask application

Routes:
 * /
 * /home
 * /ivon
 * /anna
 * /emily
 * /malvina
 * /ayishat
 * /database
 * /submit (POST request) - Accepts input via a form and displays a message on URL submit.html.

Templates:
 * All templates use template inheritance (layout.html) for a richer UI that includes a menu and responsive functionality via BootStrap 5.

Features:
 * Simple POST request, it accepts input via a form and displays the submitted data on submit.html.
 * Database integration to store and retrieve information about people and their favorite colors from the get_into_tech_c1_2025 database.

Database Connection and Operations:
data_access.py handles different passwords for Windows and Mac systems and provides the following functions:
 * get_db_connection() that connects to "get_into_tech_c1_2025" database.
 * get_people() to see a list of people and their favorite colors from the database.
 * add_person(fname, lname, col) to add a person to the database with their favourite color. If the color doesn’t exist, it adds it first.

Error handling:
 * There are also error handling templates: 404.html and 500.html.