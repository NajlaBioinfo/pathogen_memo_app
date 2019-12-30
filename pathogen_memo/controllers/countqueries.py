from flask import request, render_template, make_response
from datetime import datetime
import psycopg2
import os

#__ Configure access to .env file
from dotenv import load_dotenv
from pathlib import Path  # python3 only


def get_queries_count():

    """
    Get Pathogen Counts
    """

    #Load env 
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    dbname = os.environ.get('DBCALL')
    username = os.environ.get('DBUSER')
    password = os.environ.get('DBPASS')
    dbhost = os.environ.get('DBHOST')

    con = psycopg2.connect(database=dbname, user=username,
                    password=password, host=dbhost, port=5432)

    with con:
        cur = con.cursor()
        postgreSQL_select_Query = "SELECT * FROM pathogens"

        try:
            cur.execute(postgreSQL_select_Query)
            mappedqyery = cur.fetchall()
            pathogenscount = cur.rowcount
            return pathogenscount

        except (Exception, psycopg2.Error) as error:
            print("Database error , Counting Total of Pathogens", error)