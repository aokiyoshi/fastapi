from pydantic import BaseModel


class SongBase(BaseModel):
    name: str
    artist_id: int | None
    album_id: int | None


class SongCreate(SongBase):
    pass


class Song(SongBase):
    id: int

    class Config:
        orm_mode = True


class AlbumBase(BaseModel):
    name: str
    year: int
    artist_id: int | None
    tracklist: list[Song]  = [] 

class AlbumCreate(AlbumBase):
    pass


class Album(AlbumBase):
    id: int
    artist_id: int | None
    tracklist: list[Song]  = [] 

    class Config:
        orm_mode = True


class ArtistBase(BaseModel):
    name: str
    bio: str | None


class ArtistCreate(ArtistBase):
    pass


class Artist(ArtistBase):
    id: int

    albums: list[Album] = []
    songs: list[Song] = []

    class Config:
        orm_mode = True
