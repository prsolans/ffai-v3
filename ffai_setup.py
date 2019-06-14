from sources.source_teams import get_team_data
from sources.source_players import get_player_data
from sources.nflcom_fantasy_points import get_nfl_com_data
from sources.pro_football_reference_fantasy_points import get_pfr_fantasy_data
from utilities.utility_data import create_tables

if __name__ == '__main__':
    create_tables()
    get_team_data()
    get_player_data()
    get_nfl_com_data()
    get_pfr_fantasy_data()