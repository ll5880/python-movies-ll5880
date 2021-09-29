from timeit import default_timer as timer
import operator

def lookUp(tconst, movie, ratings) -> None:
    if tconst in movie and tconst in ratings:
        m = movie[tconst]
        r = ratings[tconst]
        print("Processing: LOOKUP ", tconst)
        start = timer()
        print("\tMOVIE: Identifier: ", m.tconst, ", Title: ", m.primaryTitle, ", Type: ",
              m.titleType, ", Year: ", m.startYear, ", Runtime: ", m.runTime, ", Genres: ", m.genres)
        print("\tRATING: Identifier: ", r.tconst, ", Rating: ", r.averageRating, ", Votes: ", r.numVotes)
        elapsed = timer() - start
        print('elapsed time (s):', elapsed, "\n")
    else:
        print("Processing: LOOKUP ", tconst)
        start = timer()
        print("\tMovie not found!")
        print("\tRating not found!")
        elapsed = timer() - start
        print('elapsed time (s):', elapsed, "\n")

