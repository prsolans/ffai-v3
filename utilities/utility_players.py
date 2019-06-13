import sqlite3
from sqlite3 import Error

from utilities.utility_data import create_connection

def find_player_id_by_name(playerName):
    """ find the player_id for an existing player in our database
    """
    try:
        conn = create_connection()
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

# DEBUGGING
# player_id = find_player_id_by_name("Dion Lewis")
# print(player_id)
