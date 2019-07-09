import sqlite3
from sqlite3 import Error
import re
import psycopg2
import os
import urllib.parse as urlparse
import csv


def create_postgresql_connection():
    try:

        # url = urlparse.urlparse(os.environ['DATABASE_URL'])
        # dbname = url.path[1:]
        # user = url.username
        # password = url.password
        # host = url.hostname
        # port = url.port

        # connection = psycopg2.connect(
        #     dbname=dbname,
        #     user=user,
        #     password=password,
        #     host=host,
        #     port=port
        #     )

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
        return(team)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def get_team_by_name(name):
    try:
        cursor = create_postgresql_connection()
        cursor.execute("SELECT * from teams WHERE name='"+name+"';")
        team = cursor.fetchone()
        return(team)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def get_team_by_abbreviation(abbreviation):
    try:
        cursor = create_postgresql_connection()
        cursor.execute("SELECT * from teams WHERE abbreviation='"+abbreviation+"';")
        team = cursor.fetchone()
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

def create_player(name, position, teamid):
    try:
        connection = psycopg2.connect(user = "prsolans",
                                    password = "",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "ffai")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM players WHERE name='"+name+"' AND position='"+position+"' AND team_id="+str(teamid)+";")
        existing = cursor.fetchone()
        print(existing)
        if existing == None:
            insert = "INSERT INTO players(name, position, team_id) VALUES ('"+name+"', '"+position+"', "+str(teamid)+");"
            print(insert)
            cursor.execute(insert)
            connection.commit()
            print('Added: ' + name)
        else:
            print('Already exists')
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)


def create_game_log(details):
    try:
        connection = psycopg2.connect(user = "prsolans",
                                    password = "",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "ffai")
        cursor = connection.cursor()
        cursor.execute(details)
        connection.commit()
        print('Added: ' + details[1])
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
        cursor.execute("SELECT * from players WHERE name='"+playername+"';")
        player = cursor.fetchone()
        return(player)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def get_player_rankings(playerid):
    try:
        cursor = create_postgresql_connection()
        cursor.execute("SELECT * from rankings WHERE player_id='"+playerid+"';")
        rankings = cursor.fetchall()
        return(rankings)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def get_player_game_log(playerid):
    try:
        cursor = create_postgresql_connection()
        cursor.execute("SELECT * from game_log WHERE player_id='"+playerid+"';")
        games = cursor.fetchall()
        return(games)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def get_player_fantasy_stats(playerid):
    try:
        cursor = create_postgresql_connection()
        cursor.execute("SELECT * from fantasy_stats WHERE player_id='"+playerid+"';")
        stats = cursor.fetchall()
        print(stats)
        return(stats)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

def create_tables():
    """ create core database tables
    """
    try:
        connection = psycopg2.connect(user = "prsolans",
                                    password = "",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "ffai")
        cursor = connection.cursor()
        cursor.execute(open("create_the_tables.sql", "r").read())
        connection.commit()
        print('Tables created...')
    except Exception as e:
        print(e)

def add_teams():
    """ create core database tables
    """
    try:
        connection = psycopg2.connect(user = "prsolans",
                                    password = "",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "ffai")
        cursor = connection.cursor()
        with open('csv/teams.csv', 'r') as f:
            cursor.copy_from(f, 'teams', sep=',')
        connection.commit()
        print('Teams added...')
    except Exception as e:
        print(e)

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

create_tables()
add_teams()
