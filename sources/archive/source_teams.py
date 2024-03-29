# Original code used to create table of NFL teams

import csv
from bs4 import BeautifulSoup

from utilities.utility_scrape import simple_get

def get_team_data():

    try:
        """## Enter the URL we are looking to crawl
        """
        raw_html = simple_get('https://www.spotrac.com/nfl/')
        html = BeautifulSoup(raw_html, 'html.parser')

        """## Get list of all the teams
        """
        teamlistTable = html.findAll("a", {"class": "team-name"})
        numOfTeams = len(teamlistTable)

        teamList = []

        print(numOfTeams)

        for i in range(0, numOfTeams):
          team = teamlistTable[i].text

          words = team.split()
          name = words[-1]
          city = team.rsplit(' ', 1)[0]
          teamData = [city, name]

          teamList.append(teamData)

        with open('csv/team.csv', 'w') as csvfile:
          filewriter = csv.writer(csvfile, delimiter=',',
                                  quotechar='|', quoting=csv.QUOTE_MINIMAL)
          for team in teamList:
            city = team[0]
            name = team[1]
            # item = '[("'+ city +'", "'+ name +'", "XXX")]'
            # print(item)
            filewriter.writerow([city, name, 'XXX'])

        # """## Create team INSERT statements
        # """
        # for team in teamList:

        #     item = 'INSERT into teams (city, name, abbreviation) VALUES ("'+ team[0] +'", "'+ team[1] +'", "XXX"); '
        #     print(item)
        #     insert_data(item)

        print('Team data inserted...')
    except Exception as e:
        print(e)

get_team_data()
