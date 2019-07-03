import sqlite3
from sqlite3 import Error
import re
import psycopg2

def create_postgresql_connection():
    try:
        connection = psycopg2.connect(user = "prsolans",
                                    password = "",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "ffai")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        # print ( connection.get_dsn_parameters(),"\n")
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        # record = cursor.fetchone()
        # print("You are connected to - ", record,"\n")
        return(cursor)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def get_teams():
    try:
        cursor = create_postgresql_connection()
        cursor.execute("SELECT * from teams;")
        rows = cursor.fetchall()
        teams = []
        for row in rows:
            teams.append(row)
        print(type(teams))
        return(teams)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    # finally:
        #closing database connection.
            # if(connection):
            #     cursor.close()
            #     connection.close()
            #     print("PostgreSQL connection is closed")

def get_team_by_id(id):
    try:
        cursor = create_postgresql_connection()
        cursor.execute("SELECT * from teams WHERE team_id="+str(id)+";")
        team = cursor.fetchone()
        # print(team)
        return(team)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def get_team_by_name(name):
    try:
        cursor = create_postgresql_connection()

        cursor.execute("SELECT * from teams WHERE name='"+name+"';")
        team = cursor.fetchone()

        print(team)
        return(team)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)


def get_players_by_team(teamid):
    try:
        cursor = create_postgresql_connection()

        cursor.execute("SELECT * from players WHERE team_id='"+teamid+"';")
        players = cursor.fetchall()

        return(players)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)


def get_player_by_id(playerid):
    try:
        cursor = create_postgresql_connection()

        cursor.execute("SELECT * from players WHERE player_id='"+playerid+"';")
        player = cursor.fetchone()

        return(player)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)


def get_player_by_name(playername):
    try:
        cursor = create_postgresql_connection()

        cursor.execute("SELECT * from players WHERE name='"+playername+"' AND position='QB';")
        player = cursor.fetchone()
        print(player)
        return(player)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def get_player_rankings(playerid):
    try:
        cursor = create_postgresql_connection()

        cursor.execute("SELECT * from rankings WHERE player_id='"+playerid+"';")
        rankings = cursor.fetchall()
        print(rankings)
        return(rankings)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)


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
