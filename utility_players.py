import sqlite3
from sqlite3 import Error

def find_player_id_by_name(playerName):
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect('ffai_1.db')
        c = conn.cursor()
        # playerName = "Julio Jones"
        player = c.execute('SELECT * from players WHERE name ="'+ playerName +'"')        
        rows = player.fetchall()
        for row in rows:
            return row[0]
    
    except Error as e:
        print(e)
    finally:
        conn.close()

# player_id = find_player_id_by_name("Dion Lewis")
# print(player_id)
