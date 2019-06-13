import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup

from utilities.utility_scrape import simple_get
from utilities.utility_players import find_player_id_by_name
from utilities.utility_data import convert_to_integer, insert_data

def get_pfr_fantasy_data():

    try:
        """## Enter the URL we are looking to crawl
        """
        raw_html = simple_get('https://www.pro-football-reference.com/years/2018/fantasy.htm')
        html = BeautifulSoup(raw_html, 'html.parser')

        """## Create list of table rows"""
        listItems = html.find("div", {"class": "table_container"}).find("table").find("tbody").findAll("tr", {"class":None})

        playerObjects = []

        for tr in listItems:
          player = {}

          playerLink = tr.find("td").find("a")
          name = playerLink.text
          url = playerLink['href']
          points = tr.find("td", {"data-stat":"fantasy_points"}).text

          ## THERE IS A GOOD SOURCE FOR CORE ANNUAL STATS
          ## THERE ARE 20+ more fields we can harvest from here
          player['id'] = find_player_id_by_name(name)
          player['points'] = convert_to_integer(points)
          player['url'] = url

          playerObjects.append(player)

        print(playerObjects)

        # This represents every player with an active contract in the NFL
        for player in playerObjects:       
            source = 'pro-football-reference'
            year = '2018'
            item = 'INSERT INTO fantasy_stats (player_id, source, year, points, url) VALUES ('+str(player['id'])+', "'+source+'", "'+year+'", '+str(player['points'])+', "'+str(player['url'])+'")'
            insert_data(item)

        print('Data successfully inserted...')    

    except Error as e:
        print(e)