import sqlite3
from sqlite3 import Error

def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect('ffai_1.db')
        print(sqlite3.version)
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
                  (contract_id INTEGER PRIMARY KEY, player_id integer, average_salary text, contract_length text, contract_terms text, guaranteed text, expiration text)''')
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
        conn = sqlite3.connect('ffai_1.db')
        c = conn.cursor()
        c.execute(data)
        conn.commit()        
    except Error as e:
        print(e)
    finally:
        conn.close()
