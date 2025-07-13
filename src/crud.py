from sqlalchemy.orm import Session
from src import models
from fastapi import HTTPException
import httpx

API_TOKEN = "d0db2391b1c20bed9dc384bb7bcc20e8"
API_URL = f"https://superheroapi.com/api/{API_TOKEN}/search"

def get_hero_by_name(db: Session, name: str):
    return db.query(models.Hero).filter(models.Hero.name == name).first()

def create_hero(db: Session, name: str):
    if get_hero_by_name(db, name):
        raise HTTPException(status_code=400, detail="Hero already exists")

    response = httpx.get(f"{API_URL}/{name}")
    data = response.json()
    if data.get("response") != "success":
        raise HTTPException(status_code=404, detail="Hero not found in API")

    hero_data = next((res for res in data["results"] if res["name"].lower() == name.lower()), None)
    if not hero_data:
        raise HTTPException(status_code=404, detail="Exact hero not found")

    stats = hero_data["powerstats"]
    hero = models.Hero(
        name=hero_data["name"],
        intelligence=int(stats.get("intelligence", 0)),
        strength=int(stats.get("strength", 0)),
        speed=int(stats.get("speed", 0)),
        power=int(stats.get("power", 0))
    )
    db.add(hero)
    db.commit()
    db.refresh(hero)
    return hero

def get_heroes(db: Session, filters: dict):
    query = db.query(models.Hero)
    if "name" in filters:
        query = query.filter(models.Hero.name == filters["name"])
    for field in ["intelligence", "strength", "speed", "power"]:
        if f"{field}__gte" in filters:
            query = query.filter(getattr(models.Hero, field) >= filters[f"{field}__gte"])
        if f"{field}__lte" in filters:
            query = query.filter(getattr(models.Hero, field) <= filters[f"{field}__lte"])
        if field in filters:
            query = query.filter(getattr(models.Hero, field) == filters[field])
    heroes = query.all()
    if not heroes:
        raise HTTPException(status_code=404, detail="No heroes match the filters")
    return heroes
