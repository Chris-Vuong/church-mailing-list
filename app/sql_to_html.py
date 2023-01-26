import os
import pandas as pd
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv()

def sqlConnection():
    cnx = mysql.connector.connect(
    host=os.getenv('host'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    port=os.getenv('port'),
    database=os.getenv('database')
    )
    return cnx


def sqlQuery():
    try:
        cnx = sqlConnection()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect password or username")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Connection sucessful")
    # Query Data TODO: fstring dynamic query. Enter once. Connection error handling
        headings = ("First Name", "Last Name", "Email")
        QUERY = "SELECT FirstName, LastName, Email FROM contacts"
        data = tuple(pd.read_sql_query(QUERY, cnx).itertuples(index=False))
        return (headings, data)