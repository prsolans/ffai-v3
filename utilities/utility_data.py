import sqlite3
from sqlite3 import Error
import re

def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect('ffai_1.db')
        return(conn)
    except Error as e:
        print(e)

def create_tables():
    """ create core database tables
    """
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS teams')
        c.execute('''CREATE TABLE IF NOT EXISTS teams
                  (team_id INTEGER PRIMARY KEY, city text, name text, abbreviation text)''')
        c.execute('DROP TABLE IF EXISTS players')
        c.execute('''CREATE TABLE IF NOT EXISTS players
                  (player_id INTEGER PRIMARY KEY, name text, age integer, experience integer, position text, team text)''')
        c.execute('DROP TABLE IF EXISTS contracts')
        c.execute('''CREATE TABLE IF NOT EXISTS contracts
                  (contract_id INTEGER PRIMARY KEY, player_id integer, average_salary integer, contract_length integer, contract_terms integer, guaranteed integer, expiration text)''')
        c.execute('DROP TABLE IF EXISTS fantasy_stats')
        c.execute('''CREATE TABLE IF NOT EXISTS fantasy_stats
                  (contract_id INTEGER PRIMARY KEY, player_id integer, source text, year text, points integer, url text)''')
        conn.commit()
        print('Tables created...')
    except Error as e:
        print(e)
    finally:
        conn.close()

def insert_data(data):
    """ create a database connection to a database and execute a statement
        data: single INSERT statement
    """
    try:
        conn = create_connection()
        c = conn.cursor()
        c.execute(data)
        conn.commit()        
    except Error as e:
        print(e)
    finally:
        conn.close()

def convert_to_integer(input):
    """ take a string value - as for a dollar amount of year amount
        and convert to an integer
    """
    try:
        intValue = re.sub('[^0-9]','', input)
        if len(intValue) < 1:
            intValue = '0'    
        intValue = int(intValue)
        return intValue
    except Error as e:
        print(e)