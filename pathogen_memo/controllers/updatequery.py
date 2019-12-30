from flask import request, render_template, make_response
from datetime import datetime
import psycopg2
import os

#__ Configure access to .env file
from dotenv import load_dotenv
from pathlib import Path  # python3 only


def get_query_by_id(id_to_update):

    """
    Get all ranks from pathogen table
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
        postgreSQL_select_Query = "SELECT * FROM pathogens WHERE id = %s"

        try:
            cur.execute(postgreSQL_select_Query, (id_to_update,))
            mappedqyery = cur.fetchall()
            return mappedqyery


        except (Exception, psycopg2.Error) as error:
            print("Error fetching data from PostgreSQL table", error)


def update_query_by_id(id_to_update, organism, taxonid, rank, gram, aerobe, habitat, isolation, pathostate):
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
        # insert data
        now=datetime.now()
        timestamp= now.strftime("%Y-%m-%d %H:%M:%S")

        #Update organism field
        sql_update_query = """Update pathogens set organism = %s where id = %s"""
        cur.execute(sql_update_query, (str(organism), id_to_update))
        print(sql_update_query,id_to_update)
        con.commit()


        #Update taxonId field
        sql_update_query = """Update pathogens set taxonid = %s where id = %s"""
        cur.execute(sql_update_query, (str(taxonid), id_to_update))
        con.commit()

        #Update rank field
        sql_update_query = """Update pathogens set rank = %s where id = %s"""
        cur.execute(sql_update_query, (str(rank), id_to_update))
        con.commit()

        #Update gram field
        sql_update_query = """Update pathogens set gram = %s where id = %s"""
        cur.execute(sql_update_query, (str(gram), id_to_update))
        con.commit()

        #Update aerobe field
        sql_update_query = """Update pathogens set aerobe = %s where id = %s"""
        cur.execute(sql_update_query, (str(aerobe), id_to_update))
        con.commit()

        #Update habitat field
        sql_update_query = """Update pathogens set habitat = %s where id = %s"""
        cur.execute(sql_update_query, (str(habitat), id_to_update))
        con.commit()

        #Update isolation field
        sql_update_query = """Update pathogens set isolation = %s where id = %s"""
        cur.execute(sql_update_query, (str(isolation), id_to_update))
        con.commit()

        #Update pathostate field
        sql_update_query = """Update pathogens set pathostate = %s where id = %s"""
        cur.execute(sql_update_query, (str(pathostate), id_to_update))
        con.commit()

        #Update taxonId field
        sql_update_query = """Update pathogens set timestamp = %s where id = %s"""
        cur.execute(sql_update_query, (str(timestamp), id_to_update))
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