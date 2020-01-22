
import psycopg2
import os

#__ Configure access to .env file
from dotenv import load_dotenv
from pathlib import Path  # python3 only

def getjsonfile(fileds, tablename, filename):
    """
    Get all rows table
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
        cur.execute("COPY (SELECT array_to_json(array_agg(row_to_json (r))) \
          FROM ( SELECT " + fileds + " FROM " + tablename + " ) r) TO '" + filename + "'")
    con.close()
    return filename

