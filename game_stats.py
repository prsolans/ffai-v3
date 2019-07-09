import csv
from bs4 import BeautifulSoup

from utilities.utility_data import convert_to_integer, get_team_by_name, get_team_by_abbreviation, get_player_by_name, create_player, create_game_log
from utilities.utility_scrape import simple_get


def get_player_links():

    try:
        """## Get page from PFR
        """
        raw_html = simple_get('https://www.pro-football-reference.com/years/2018/passing.htm#passing::pass_att')
        html = BeautifulSoup(raw_html, 'html.parser')
        # print(html)
        """## Get all 2018 NFL passers
        """
        playerRows = html.find('table', {'id': 'passing'}).find('tbody').findAll('tr', {'class': None})

        playerLinks = []
        for row in range(len(playerRows)):
          td_list = playerRows[row].findAll('td')
          playerLink = td_list[0].find('a')['href']
          playerLinks.append(playerLink)

        return playerLinks

    except Exception as e:
        print(e)

def get_player_data():

    try:

        playerLinks = get_player_links()

        print(len(playerLinks))

        for row in range(len(playerLinks)):
          thisLink = 'https://www.pro-football-reference.com/' + playerLinks[row]
          thisLink = thisLink[:-4]
          thisLink = thisLink + '/gamelog/2018/'
          raw_html = simple_get(thisLink)
          html = BeautifulSoup(raw_html, 'html.parser')

          playerName = html.find('h1', {'itemprop': 'name'}).text
          playerPosition = html.find('div', {'itemtype': 'https://schema.org/Person'}).findAll('p')[1].text
          playerPosition = playerPosition.split()[1]

          if html.find('span', {'itemprop': 'affiliation'}) is not None:
            playerTeam = html.find('span', {'itemprop': 'affiliation'}).find('a').text
            playerTeam = playerTeam.split()
            playerTeam = get_team_by_name(playerTeam[-1])[0]
          else:
            playerTeam = 33


          print(playerName, playerPosition, playerTeam)

          # create_player(playerName, playerPosition, playerTeam)
          gameRows = html.find('table', {'id': 'stats'}).find('tbody').findAll('tr')

          for row in range(len(gameRows)):
            td_list = gameRows[row].findAll('td')
            gDate = td_list[0].text
            gLocation = td_list[4].text
            gOpponent = td_list[5].text
            gResult = td_list[6].text
            gPassComplete = td_list[8].text
            gPassAttempt = td_list[9].text
            gPassPercentage = td_list[10].text
            gPassYds = td_list[11].text
            gPassTD = td_list[12].text
            gPassINT = td_list[13].text
            gPassRating = td_list[14].text
            gPassSack = td_list[15].text
            gPassSackYds = td_list[16].text
            gPassYdsPerAttempt = td_list[17].text
            gPassAdjYdsPerAttempt = td_list[18].text
            # gRushAttempt = td_list[19].text
            # gRushYds = td_list[20].text
            # gRushYdsPerAttempt = td_list[21].text
            # gRushTD = td_list[22].text
            # gRecTargets = td_list[23].text
            # gRec = td_list[24].text
            # gRecYds = td_list[25].text
            # gRecYdsPerRec = td_list[26].text
            # gRecTD = td_list[27].text
            # gCatchPercentage = td_list[28].text
            # gRecYdsPerTarget = td_list[29].text
            # gAllTD = td_list[30].text
            # gPoints = td_list[31].text
            # gFumbles = td_list[32].text

            gPlayerId = get_player_by_name(playerName)[0]
            gOpponent = get_team_by_abbreviation(gOpponent)[0]

            # print(gPlayerId, gDate, gLocation, gOpponent, gResult, gPassComplete, gPassAttempt, gPassPercentage, gPassYds, gPassTD, gPassINT, gPassRating, gPassSack, gPassSackYds, gPassYdsPerAttempt, gPassAdjYdsPerAttempt, gRushAttempt, gRushYds, gRushYdsPerAttempt, gRushTD, gRecTargets, gRec, gRecYds, gRecYdsPerRec, gRecTD, gCatchPercentage, gRecYdsPerTarget, gAllTD, gPoints, gFumbles)

            # print("INSERT INTO game_log (player_id, game_location, opponent, game_result, pass_cmp, pass_att, pass_cmp_perc, pass_yds, pass_td, pass_int, pass_rating, pass_sacked, pass_sacked_yds, pass_yds_per_att, pass_adj_yds_per_att, rush_att, rush_yds, rush_yds_per_att, rush_td, targets, rec, rec_yds, rec_yds_per_rec, rec_td, catch_pct, rec_yds_per_tgt, all_td, scoring, fumbles, game_date) VALUES ("+str(gPlayerId)+", '"+gDate+"', '"+gLocation+"', "+str(gOpponent)+", '"+gResult+"', "+str(gPassComplete)+", "+str(gPassAttempt)+", "+str(gPassPercentage)+", "+str(gPassYds)+", "+str(gPassTD)+", "+str(gPassINT)+", "+str(gPassRating)+", "+str(gPassSack)+", "+str(gPassSackYds)+", "+str(gPassYdsPerAttempt)+", "+str(gPassAdjYdsPerAttempt)+", "+str(gRushAttempt)+", "+str(gRushYds)+", "+str(gRushYdsPerAttempt)+", "+str(gRushTD)+", "+str(gRecTargets)+", "+str(gRec)+", "+str(gRecYds)+", "+str(gRecYdsPerRec)+", "+str(gRecTD)+", "+str(gCatchPercentage)+", "+str(gRecYdsPerTarget)+", "+str(gAllTD)+", "+str(gPoints)+", "+str(gFumbles)+");")

            print(gPlayerId, gDate, gLocation, gOpponent, gResult, gPassComplete, gPassAttempt, gPassPercentage, gPassYds, gPassTD, gPassINT, gPassRating, gPassSack, gPassSackYds, gPassYdsPerAttempt, gPassAdjYdsPerAttempt)

            details = "INSERT INTO game_log (player_id, game_location, opponent, game_result, pass_cmp, pass_att, pass_cmp_perc, pass_yds, pass_td, pass_int, pass_rating, pass_sacked, pass_sacked_yds, pass_yds_per_att, pass_adj_yds_per_att, game_date) VALUES ("+str(gPlayerId)+", '"+gLocation+"', "+str(gOpponent)+", '"+gResult+"', "+str(gPassComplete)+", "+str(gPassAttempt)+", "+str(gPassPercentage)+", "+str(gPassYds)+", "+str(gPassTD)+", "+str(gPassINT)+", "+str(gPassRating)+", "+str(gPassSack)+", "+str(gPassSackYds)+", "+str(gPassYdsPerAttempt)+", "+str(gPassAdjYdsPerAttempt)+", '"+gDate+"');"

            create_game_log(details)

        return playerLinks

    except Exception as e:
        print(e)

get_player_data()

