import sqlite3
from sqlite3 import Error

from utilities.utility_data import create_connection

def find_player_id_by_name(playerName):
    """ find the player_id for an existing player in our database
    """
    try:
        conn = create_connection()
        c = conn.cursor()
        # print(playerName)
        player = c.execute('SELECT * from players WHERE name ="'+ playerName +'"')
        row = player.fetchone()
        print(row)
        return(row)

    except Exception as e:
        print(e)
    finally:
        conn.close()

# DEBUGGING
# player_id = find_player_id_by_name("Dion Lewis")
# print(player_id)
