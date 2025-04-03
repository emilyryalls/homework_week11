import mysql.connector
import sys

if sys.platform == "win32":
    mysql_password = "password"
else:
    mysql_password = ""

def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=mysql_password,
        database="get_into_tech_c1_2025"
    )
    return mydb

def get_people():
    # like connecting to the server of the database
    conn = get_db_connection() # stablish connection with DB server and DB called "get_into_tech_c1_2025"
                                # using user name root...
    # like opening a query window
    cursor = conn.cursor()  # call its cursor method, which gives it the abilities to send commands

    sql = "Select firstname, lastname, FavouriteColour from vfavouritecolours" # selecting the first name...
    cursor.execute(sql) # and the executing them
    # like clicking on the lightning bolt in mysql workbench

    result_set = cursor.fetchall() #cursor object, to fetch all that info
    person_list = [] # we run a loop to save all the rows on a list - on 0 is stored the name, on 1 the last name and on 2 the colour
                        #list were each row will be a dictionary item with keays
    for item in result_set:
        person_list.append({'firstname': item[0], 'lastname': item[1], 'FavouriteColour': item[2]})
    return person_list


def add_person(fname, lname, col):
    conn = get_db_connection()
    cursor = conn.cursor()

    #checkk if colour exist
    sql_check_colour = "SELECT ColourID FROM colour WHERE Name = %s" # the %s the s is for string
    cursor.execute(sql_check_colour, (col,)) ## execute above query passing the colour to the placeholder %s
                                                    ## passing tuple because cursor.execute expect an iterable
    colour_result = cursor.fetchone() # hold the most recent query result if true, if false then return None

    if colour_result: # if true then save it in below variable
        colour_id = colour_result[0]
    else:
        # if colour doesn't exist, insert it and get its id
        sql_insert_colour = "INSERT INTO colour (Name) VALUES (%s)"
        cursor.execute(sql_insert_colour, (col,))
        colour_id = cursor.lastrowid

    sql_person = "INSERT INTO person (firstname, lastname, ColourID) VALUES (%s, %s, %s)"
    val = (fname, lname, colour_id)
    cursor.execute(sql_person, val)

    conn.commit() # it commit the info into the DB