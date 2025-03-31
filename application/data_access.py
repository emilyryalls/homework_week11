import mysql.connector
import sys

if sys.platform == "win32":
    mysql_password = "password"
else:
    mysql_password = ""

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=mysql_password,
#   database="get_into_tech_c1_2025"
# )

def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=mysql_password,
        database="get_into_tech_c1_2025"
    )
    return mydb


def get_people():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "Select firstname, lastname, FavouriteColour from vfavouritecolours"
    cursor.execute(sql)

    result_set = cursor.fetchall()
    person_list = []
    for vfavouritecolours in result_set:
        person_list.append({'firstname': vfavouritecolours[0], 'lastname': vfavouritecolours[1], 'FavouriteColour': vfavouritecolours[2]})
    return person_list


def add_person(fname, lname, col):
    conn = get_db_connection()
    cursor = conn.cursor()

    #checkk if colour exist
    sql_check_colour = "SELECT ColourID FROM colour WHERE Name = %s"
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

    conn.commit()