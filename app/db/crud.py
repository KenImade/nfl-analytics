"""SQLAlchemy Query Functions"""

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from datetime import date

from app.db import models


def get_player(db: Session, player_id: int):
    """
    Queries the datbase and retrieves the specified player
    information using the <player_id> if found.
    """
    return db.query(models.Player).filter(models.Player.player_id == player_id).first()


def get_players(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    min_last_changed_date: date = None,
    last_name: str = None,
    first_name: str = None,
):
    """
    Queries the database and retrieves a multiple players infromation
    as a list. Can retrieve as many players as needed. Default limit is
    100.
    """
    query = db.query(models.Player)

    if min_last_changed_date:
        query = query.filter(models.Player.last_changed_date >= min_last_changed_date)

    if first_name:
        query = query.filter(models.Player.first_name == first_name)

    if last_name:
        query = query.filter(models.Player.last_name == last_name)

    return query.offset(skip).limit(limit).all()


def get_performances(
    db: Session, skip: int = 0, limit: int = 100, min_last_changed_date: date = None
):
    """
    Docstring for get_performances

    :param db: Description
    :type db: Session
    :param skip: Description
    :type skip: int
    :param limit: Description
    :type limit: int
    :param min_last_changed_date: Description
    :type min_last_changed_date: date
    """
    query = db.query(models.Performance)
    if min_last_changed_date:
        query = query.filter(
            models.Performance.last_changed_date >= min_last_changed_date
        )
    return query.offset(skip).limit(limit).all()


def get_league(db: Session, league_id: int = None):
    """
    Docstring for get_league

    :param db: Description
    :type db: Session
    :param league_id: Description
    :type league_id: int
    """
    return db.query(models.League).filter(models.League.league_id == league_id).first()


def get_leagues(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    min_last_changed_date: date = None,
    league_name: str = None,
):
    """
    Docstring for get_leagues

    :param db: Description
    :type db: Session
    :param skip: Description
    :type skip: int
    :param limit: Description
    :type limit: int
    :param min_last_changed_date: Description
    :type min_last_changed_date: date
    :param league_name: Description
    :type league_name: str
    """
    query = db.query(models.League).options(joinedload(models.League.teams))
    if min_last_changed_date:
        query = query.filter(models.League.last_changed_date >= min_last_changed_date)

    if league_name:
        query = query.filter(models.League.league_name == league_name)

    return query.offset(skip).limit(limit).all()


def get_teams(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    min_last_changed_date: date = None,
    team_name: str = None,
    league_id: int = None,
):
    """
    Docstring for get_teams

    :param db: Description
    :type db: Session
    :param skip: Description
    :type skip: int
    :param limit: Description
    :type limit: int
    :param min_last_changed_date: Description
    :type min_last_changed_date: date
    :param team_name: Description
    :type team_name: str
    :param league_id: Description
    :type league_id: int
    """
    query = db.query(models.Team)

    if min_last_changed_date:
        query = query.filter(models.Team.last_changed_date >= min_last_changed_date)

    if team_name:
        query = query.filter(models.Team.team_name == team_name)

    if league_id:
        query = query.filter(models.Team.league_id == league_id)

    return query.offset(skip).limit(limit).all()


# analytics queries
def get_player_count(db: Session):
    """
    Docstring for get_player_count

    :param db: Description
    :type db: Session
    """
    query = db.query(models.Player)
    return query.count()


def get_team_count(db: Session):
    """
    Docstring for get_team_count

    :param db: Description
    :type db: Session
    """
    query = db.query(models.Team)
    return query.count()


def get_league_count(db: Session):
    """
    Docstring for get_league_count

    :param db: Description
    :type db: Session
    """
    query = db.query(models.League)
    return query.count()
