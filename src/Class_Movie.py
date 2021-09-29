from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    tconst: str
    titleType: str
    primaryTitle: str
    startYear: int
    endYear: int
    runTime: int
    genres: list
