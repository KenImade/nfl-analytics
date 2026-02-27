"""Contains the configurations for the API"""

from pathlib import Path

API_VERSION = "v0"
BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "db" / "fantasy_data.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"
