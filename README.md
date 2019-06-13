README.md

#FFAI v3

Our goal is to build a superior algorithm for comparing the relative fantasy football value of NFL players.

* ffai_setup.py - This file initiates the process

### Setup
#### We should have one for each data source
* setup_players.py - Scrapes and inserts player and contract data
* setup_teams.py - Scrapes and inserts team data

### Utilities
#### These hold the functions we use to build the DB and to leverage the data
* utility_data.py - Functions for manipulation the database and the data
* utility_players.py - Functions for interacting with player data
* utility_scrape.py - Functions for collecting and manipulating HTML