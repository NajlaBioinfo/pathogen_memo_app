from flask import request, render_template, make_response
from datetime import datetime
import psycopg2
import os

#__ Configure access to .env file
from dotenv import load_dotenv
from pathlib import Path  # python3 only


def get_query_count(criteria, criteriaval):
    """
    count query depend on criteria
    """

    dbname = os.environ.get('DBCALL')
    username = os.environ.get('DBUSER')
    password = os.environ.get('DBPASS')
    dbhost = os.environ.get('DBHOST')

    try:
        con = psycopg2.connect(database=dbname, user=username, password=password, host=dbhost, port=5432)
        cur =  con.cursor() # cursor

        count_select_Query = "SELECT * FROM pathogens WHERE " + criteria + " = %s" 
        print(count_select_Query)
        cur.execute(count_select_Query, (criteriaval,))
        getfetchedqueries = cur.fetchall()
        countquerycriteria = cur.rowcount

        messageOk="Ok, count: " + str(countquerycriteria) + " # " + criteria + " = " + criteriaval+ " Query."
        print(messageOk)
        return countquerycriteria
    
    except con.Error as err: # if error
        messageOk="Database error"
        print(messageOk)
        return messageOk
    
    finally:
        con.close() # close the connection