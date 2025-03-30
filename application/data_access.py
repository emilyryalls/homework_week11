import mysql.connector
import sys

if sys.platform == "win32":
    mysql_password = "password"
else:
    mysql_password = ""

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=mysql_password,
  database="get_into_tech_c1_2025"
)


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

