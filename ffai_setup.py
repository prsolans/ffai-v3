import sqlite3
from sqlite3 import Error

from sources.source_teams import get_team_data
from sources.source_players import get_player_data
from utilities.utility_data import create_tables

if __name__ == '__main__':
    create_tables()
    get_team_data()
    get_player_data()
