import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
from config import config
import os
import pandas as pd
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


def configure():
    '''Configures .env'''
    load_dotenv()


# Establish connection to database
try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorrect password or username")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connection sucessful")

# Query the database and save pandas dataframe
QUERY = "SELECT FirstName, LastName, Email FROM contacts"
result = pd.read_sql_query(QUERY, cnx)
print(result.loc[0]["Email"])


def subscribeList(result):
    '''Takes a sql contact query and
    adds to mailchimp mailing list via api'''
    for i in range(0, len(result)):
        try:
            client = MailchimpMarketing.Client()
            client.set_config({
                "api_key": os.getenv('api_key'),
                "server": os.getenv('server_id')
            })
            response = client.lists.add_list_member(
                os.getenv('list_id'),
                {"email_address": result.loc[i]["Email"],
                 "status": "unsubscribed",
                 "merge_fields": {
                    "FNAME": result.loc[i]["FirstName"],
                    "LNAME": result.loc[i]["LastName"]
                }
                })
            print("Email successfully added to list!")
        except ApiClientError as error:
            print("Error: {}".format(error.text))


def main():
    configure()
    subscribeList(result)


if __name__ == "__main__":
    main()
