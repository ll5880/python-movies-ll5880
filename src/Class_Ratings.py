from dataclasses import dataclass


@dataclass(frozen=True)
class Ratings:
    tconst: str
    averageRating: float
    numVotes: int
