"""Defines routes and controls for API"""

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from datetime import date

import app.schemas as schemas
from app.db import crud
from app.db.database import SessionLocal

from app.settings import API_VERSION


app = FastAPI()
router = APIRouter(prefix=f"/{API_VERSION}")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "API health check successful"}


@router.get("/players/", response_model=list[schemas.Player])
def read_players(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: date = None,
    first_name: str = None,
    last_name: str = None,
    db: Session = Depends(get_db),
):
    players = crud.get_players(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        first_name=first_name,
        last_name=last_name,
    )
    return players


@router.get("/players/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    player = crud.get_player(db, player_id=player_id)

    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")

    return player


@router.get("/performances/", response_model=list[schemas.Performance])
def read_performances(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: date = None,
    db: Session = Depends(get_db),
):
    performances = crud.get_performances(
        db, skip=skip, limit=limit, min_last_changed_date=minimum_last_changed_date
    )
    return performances


@router.get("/leagues/", response_model=list[schemas.League])
def read_leagues(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: date = None,
    league_name: str = None,
    db: Session = Depends(get_db),
):
    leagues = crud.get_leagues(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        league_name=league_name,
    )
    return leagues


@router.get("/leagues/{league_id}", response_model=schemas.League)
def read_league(league_id: int, db: Session = Depends(get_db)):
    league = crud.get_league(db, league_id=league_id)
    if league is None:
        raise HTTPException(status_code=404, detail="League not found")
    return league


@router.get("/teams/", response_model=list[schemas.Team])
def read_teams(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: date = None,
    team_name: str = None,
    league_id: int = None,
    db: Session = Depends(get_db),
):
    teams = crud.get_teams(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        team_name=team_name,
        league_id=league_id,
    )
    return teams


@router.get("/counts/", response_model=schemas.Counts)
def get_count(db: Session = Depends(get_db)):
    counts = schemas.Counts(
        league_count=crud.get_league_count(db),
        team_count=crud.get_team_count(db),
        player_count=crud.get_player_count(db),
    )
    return counts


app.include_router(router)
