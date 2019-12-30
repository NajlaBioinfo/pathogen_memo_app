from flask import request, render_template, make_response
from datetime import datetime
import psycopg2
import os

#__ Configure access to .env file
from dotenv import load_dotenv
from pathlib import Path  # python3 only

#from models import Pathogen
#from pathogen_memo import db


def organism_list():
    """
    Get all organisms form pathogen table
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
        cur.execute("SELECT organism FROM pathogens")
        organisms = cur.fetchall()
        #print(organisms)
        #return organisms
    organismslist=[]
    for organ in organisms:
        organismslist.append(organ[0])
    print(organismslist)
    return organismslist

def taxon_list():
    """
    Get all taxonids from pathogen table
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
        cur.execute("SELECT taxonid FROM pathogens")
        taxonids = cur.fetchall()

    taxonslist=[]
    for taxa in taxonids:
        taxonslist.append(taxa[0])
    print(taxonslist)
    return taxonslist




def get_lastindex():

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
        cur.execute("SELECT id FROM pathogens")
        ids = cur.fetchall()
    
    idslist=[]
    for id in ids:
        #print (id[0])
        idslist.append(id[0])

    
    last_index = max(idslist)
    #New index
    new_index= int(last_index) + 1
    return new_index


def check_if_pathogen_exist(organism, rank):
    #pathogen_is_in=False
    get_organisms= organism_list()
    get_taxons= taxon_list()

    if ( (organism in get_organisms) or (rank in get_taxons) ):
        pathogen_is_in = True
        print("pathogen_is_in", pathogen_is_in)
        return pathogen_is_in
    else:
        pathogen_is_in = False
        print("pathogen_is_in", pathogen_is_in)
        return pathogen_is_in


def save_changes(organism, taxonid, rank, gram, aerobe, habitat, isolation, pathostate):
    """
    Save the changes to the database
    """

    dbname = os.environ.get('DBCALL')
    username = os.environ.get('DBUSER')
    password = os.environ.get('DBPASS')
    dbhost = os.environ.get('DBHOST')

    try:
        con = psycopg2.connect(database=dbname, user=username, password=password, host=dbhost, port=5432)
        c =  con.cursor() # cursor
        # insert data
        now=datetime.now()
        timestamp= now.strftime("%Y-%m-%d %H:%M:%S")
        new_index = get_lastindex()

        part1_a = "INSERT INTO pathogens (id, organism, taxonid, rank, gram, aerobe, habitat, isolation, pathostate,timestamp)"
        part1_b=  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        part1 = part1_a + part1_b
        
        organism_s = str(organism)
        taxonid_s = str(taxonid)
        rank_s  = str(rank)
        gram_s  = str(gram)
        aerobe_s  = str(aerobe)
        habitat_s  = str(habitat)
        isolation_s = str(isolation)
        pathostate_s = str(pathostate)
        timestamp_s = timestamp

        part2 = (new_index,
                organism_s,
                taxonid_s,
                rank_s,
                gram_s, 
                aerobe_s,
                habitat_s,
                isolation_s,
                pathostate_s,
                timestamp_s
            )
        print (part1,part2)
        c.execute(part1,part2)
        
        con.commit() # apply changes
        
        messageOk="Ok"
        print(messageOk)
        return messageOk
    
    except con.Error as err: # if error
        messageOk="Database error"
        print(messageOk)
        return messageOk
    
    finally:
        con.close() # close the connection
