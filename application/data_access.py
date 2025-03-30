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
        database="persondb"
    )
    return mydb