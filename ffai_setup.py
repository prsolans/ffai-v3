import sqlite3
from sqlite3 import Error

from setup_teams import get_team_data
from setup_players import get_player_data
from utility_data import create_tables

if __name__ == '__main__':
    create_tables()
    get_team_data()
    get_player_data()
