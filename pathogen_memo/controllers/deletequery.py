from flask import request, render_template, make_response
from datetime import datetime
import psycopg2
import os

#__ Configure access to .env file
from dotenv import load_dotenv
from pathlib import Path  # python3 only


def delete_query_by_id(id_to_update):
    """
    Commit the changes to the database
    """

    dbname = os.environ.get('DBCALL')
    username = os.environ.get('DBUSER')
    password = os.environ.get('DBPASS')
    dbhost = os.environ.get('DBHOST')

    try:
        con = psycopg2.connect(database=dbname, user=username, password=password, host=dbhost, port=5432)
        cur =  con.cursor() # cursor

        #Delete row
        sql_delete_query = """DELETE FROM pathogens WHERE id = %s"""
        cur.execute(sql_delete_query, (id_to_update,))
  
        print(sql_delete_query,id_to_update)
        con.commit()

        messageOk="Ok"
        print(messageOk)
        return messageOk
    
    except con.Error as err: # if error
        messageOk="Database error"
        print(messageOk)
        return messageOk
    
    finally:
        con.close() # close the connection

