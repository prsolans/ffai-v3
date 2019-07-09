# import sqlite3
# from sqlite3 import Error
from bs4 import BeautifulSoup
import csv

from utilities.utility_scrape import simple_get
from utilities.utility_players import find_player_id_by_name
from utilities.utility_data import convert_to_integer, get_player_by_name

def get_nfl_com_data():

    try:
        """## Enter the URL we are looking to crawl
        """
        raw_html = simple_get('https://fantasy.nfl.com/research/scoringleaders')
        html = BeautifulSoup(raw_html, 'html.parser')

        """## Create list of table rows"""
        listItems = html.find("div", {"class": "tableWrap"}).find("table").find("tbody").findAll("tr")

        playerObjects = []

        for tr in listItems:
          player = {}
          playerLink = tr.find("td", {"class":"playerNameAndInfo"}).find("a")
          name = playerLink.text
          url = playerLink['href']
          points = tr.find("td", {"class":"statTotal"}).text
          playerObject = get_player_by_name(name)
          # print(player)
          player['id'] = playerObject[0]
          player['points'] = convert_to_integer(points)
          player['url'] = url
          playerObjects.append(player)

        # print(playerObjects)

        with open('csv/nflcom_2018_fantasypts.csv', 'w') as csvfile:
          filewriter = csv.writer(csvfile, delimiter=',',
                                  quotechar='|', quoting=csv.QUOTE_MINIMAL)

          for player in playerObjects:
            source = 'nfl'
            year = '2018'
            player_id = player['id']
            points = player['points']
            url = player['url']
            filewriter.writerow([player_id, source, year, points, url])


        # # This represents every player with an active contract in the NFL
        # for player in playerObjects:
        #     source = 'nfl'
        #     year = '2018'
        #     item = 'INSERT INTO fantasy_stats (player_id, source, year, points, url) VALUES ('+str(player['id'])+', "'+source+'", "'+year+'", '+str(player['points'])+', "'+str(player['url'])+'")'
        #     insert_data(item)

        print('Data successfully inserted...')

    except Exception as e:
        print('get_nfl_com_data: ', e)

get_nfl_com_data()
