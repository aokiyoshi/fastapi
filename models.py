from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    bio = Column(String, unique=True, index=True)

    songs = relationship("Song", back_populates="artist")
    albums = relationship("Album", back_populates="artist")


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    year = Column(Integer, unique=False, index=True)

    tracklist = relationship("Song", back_populates="album")
    artist = relationship("Artist", back_populates="albums")


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    album_id = Column(Integer, ForeignKey("albums.id"))

    album = relationship("Album", back_populates="tracklist")
    artist = relationship("Artist", back_populates="songs")
    
    


