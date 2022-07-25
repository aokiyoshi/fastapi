from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import crud
import schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Songs

@app.get("/songs", response_model=List[schemas.Song])
def read_songs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    songs = crud.get_songs(db, skip=skip, limit=limit)
    return songs


@app.get("/songs/{song_name}", response_model=schemas.Song)
def read_song_by_name(song_name: str, db: Session = Depends(get_db)):
    db_song = crud.get_song_by_name(db, song_name=song_name)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song


@app.post("/songs/create", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    return crud.create_songs(db=db, song=song)


# Artists

@app.get("/artists", response_model=List[schemas.Artist])
def read_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    artists = crud.get_artists(db, skip=skip, limit=limit)
    return artists


@app.post("/artists/create", response_model=schemas.Artist)
def create_artist(artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    db_artist = crud.get_artist(db, artist_name=artist.name)
    if db_artist:
        raise HTTPException(status_code=400, detail="Artist already exsists")
    return crud.create_artist(db=db, artist=artist)


# Albums

@app.get("/albums", response_model=List[schemas.Album])
def read_albums(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    albums = crud.get_albums(db, skip=skip, limit=limit)
    return albums


@app.post("/albums/create", response_model=schemas.Song)
def create_album(album: schemas.AlbumCreate, db: Session = Depends(get_db)):
    return crud.create_album(db=db, album=album)
