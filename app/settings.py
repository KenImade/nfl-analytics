"""Contains the configurations for the API"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_FILE = BASE_DIR / "db" / "fantasy_data.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"

API_URL_VERSION = "v0"
API_VERSION = "0.1"
API_TITLE = "Sports World Central (SWC) Fantasy Football API"
API_DESCRIPTION = """
This API provides read-only access to info from the Sports World Central (SWC) Fantasy Football API. 
The endpoints are grouped into the following categories:

## Analytics
Get information about health of the API and counts of leagues, teams, and players.

## Player
You can get a list of an NFL players, or search for an individual player by player_id.

## Scoring
You can get a list of NFL player performances, including the fantasy points they scored using SWC league scoring.

## Membership
Get information about all the SWC fantasy football leagues and the teams in them.
"""
