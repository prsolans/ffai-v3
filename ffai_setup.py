from flask import Flask, render_template
import os
import logging
import psycopg2

# from sources.source_teams import get_team_data
# from sources.source_players import get_player_data
# from sources.nflcom_fantasy_points import get_nfl_com_data
# from sources.pro_football_reference_fantasy_points import get_pfr_fantasy_data
from utilities.utility_data import create_postgresql_connection, get_teams, get_team_by_id, get_players_by_team, get_player_by_id, get_player_rankings, get_player_fantasy_stats, get_player_game_log

app = Flask(__name__)

@app.route('/')
def index():
    # create_tables()
    # get_team_data()
    # get_player_data()
    # get_nfl_com_data()
    # get_pfr_fantasy_data()
    return render_template('index.html')


@app.route('/players')
def players():
    return render_template('players.html')

@app.route('/player/<playerid>')
def player(playerid=''):
    player = get_player_by_id(playerid)
    team = get_team_by_id(player[5])
    rankings = get_player_rankings(playerid)
    fantasy_stats = get_player_fantasy_stats(playerid)
    game_log = get_player_game_log(playerid)
    return render_template('player.html', player=player, team=team, rankings=rankings, fantasy_stats=fantasy_stats, game_log=game_log)

@app.route('/teams')
def teams():
    teams = get_teams()
    return render_template('teams.html', teams=teams)

@app.route('/team/<teamid>')
def team(teamid=''):
    team = get_team_by_id(teamid)
    players = get_players_by_team(teamid)
    return render_template('team.html', team=team, players=players)

if __name__ == '__main__':
    app.run()
