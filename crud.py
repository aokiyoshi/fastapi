from sqlalchemy.orm import Session

import models
import schemas


# Songs CRUD

def get_song_by_name(db: Session, song_name: str):
    return db.query(models.Song).filter(models.Song.name == song_name).first()


def get_songs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Song).offset(skip).limit(limit).all()


def create_songs(db: Session, song: schemas.SongCreate):
    db_song = models.Song(
        name=song.name, artist_id=song.artist_id, album_id=song.album_id)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song


# Album CRUD

def create_album(db: Session, album: schemas.AlbumCreate):
    db_artist = models.Album(name=album.name, year=album.year)
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist


def get_album(db: Session, album_name: str):
    return db.query(models.Album).filter(models.Album.name == album_name).first()


def get_albums(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Album).offset(skip).limit(limit).all()


# Artists CRUD

def get_artist(db: Session, artist_name: str):
    return db.query(models.Artist).filter(models.Artist.name == artist_name).first()


def get_artists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artist).offset(skip).limit(limit).all()


def create_artist(db: Session, artist: schemas.ArtistCreate):
    db_artist = models.Artist(name=artist.name, bio=artist.bio)
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist
