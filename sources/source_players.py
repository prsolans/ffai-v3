import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup

from utilities.utility_data import insert_data
from utilities.utility_scrape import simple_get
from utilities.utility_players import find_player_id_by_name


def get_player_data():

    try:
        """## Enter the URL we are looking to crawl
        """
        raw_html = simple_get('https://www.spotrac.com/nfl/')
        html = BeautifulSoup(raw_html, 'html.parser')

        """## Create list of links to Contract pages"""

        teamlistItems = html.findAll("div", {"class": "teamoption"})

        contractPageLinks = []

        for div in teamlistItems:
          firstA = div.a.get('href')
          if "contracts" in firstA:
            contractPageLinks.append(firstA)    

        """## Retrieving the contract table data"""


        def getContractData(html):
          raw_html = simple_get(html)
          html = BeautifulSoup(raw_html, 'html.parser') 
          
          teamName = parseTeamName(html.find('div', {'class': 'team-name'}).text)
          
          contractTable = html.find("div", {"class": "teams"}).findAll("tr")
          numOfPlayers = len(contractTable)
          
          # Create an array to hold all the playerData
          playerData = []
          
          for row in range(1,numOfPlayers):
            td_list = contractTable[row].find_all("td")
            
            # Create a dictionary for a "Player", and add the data
            player = {}
            
            playerName = td_list[0].find("a").text
            playerPosition = td_list[1].text
            playerAge = td_list[2].text
            playerExperience = td_list[3].text
            playerContractTerms = td_list[4].find("span", {"class": "terms"}).text
            playerContractLength = td_list[4].find("span", {"class": "length"}).text    
            playerAverageSalary = td_list[5].text
            playerGuaranteed = td_list[6].text
            playerExpires = td_list[7].text
            
            player['team'] = teamName
            player['name'] = playerName
            player['position'] = playerPosition
            player['age'] = playerAge
            player['experience'] = playerExperience
            player['averageSalary'] = playerAverageSalary
            player['contractLength'] = playerContractLength
            player['contractTerms'] = playerContractTerms
            player['guaranteedSalary'] = playerGuaranteed
            player['contractExpiration'] = playerExpires
            
            # Add this "Player" definition to the playerData array
            playerData.append(player)
          
          return playerData

        def parseTeamName(string):
          teamName = string.replace(' Contracts', '')
          return teamName
                      
        # FOR TESTING PURPOSES
        # testUrl = 'https://www.spotrac.com/nfl/tennessee-titans/contracts/'
        # playerData = getContractData(testUrl)
        # END FOR TESTING PURPOSES

        # """## Cycle through list of Contract pages and get back all line items"""

        playerData = []

        for contractPage in contractPageLinks:
          playerData.extend(getContractData(contractPage))
          
        # This represents every player with an active contract in the NFL
        for player in playerData:
            item = 'INSERT INTO players (name, age, experience, position, team) VALUES ("'+player['name']+'", "'+player['age']+'", "'+player['experience']+'", "'+player['position']+'", "'+player['team']+'" )'
            insert_data(item)

        print('Player data inserted...')

        # This represents every player with an active contract in the NFL
        for player in playerData:            
            playerId = find_player_id_by_name(player['name'])
            item = 'INSERT INTO contracts (player_id, average_salary, contract_length, contract_terms, guaranteed, expiration) VALUES ('+str(playerId)+', "'+player['averageSalary']+'", "'+player['contractLength']+'", "'+player['contractTerms']+'", "'+player['guaranteedSalary']+'", "'+player['contractExpiration']+'" )'
            insert_data(item)

        print('Player contract data inserted...')    

    except Error as e:
        print(e)

