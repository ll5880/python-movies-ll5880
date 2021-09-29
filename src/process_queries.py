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

def Contains(titleType, words, movie) -> None:
    print("processing: CONTAINS ", titleType, words)
    start = timer()
    found = False
    movieList = []
    for key in movie:
        if titleType == movie[key].titleType:
            m = movie[key]
            if words in m.primaryTitle:
                found = True
                movieList.append(movie[key])

    if not found:
        print("\tNo match found!")
    else:
        for m in movieList:
            print("\tIdentifier: ", m.tconst, ", Title: ", m.primaryTitle, ", Type: ", m.titleType,
                  ", Year: ", m.startYear, ", Runtime: ", m.runTime, ", Genres: ", m.genres)

    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")


def Year_and_Genre(titleType, startYear, genre, movie) -> None:
    print("processing: YEAR_AND_GENRE ", titleType, startYear, genre)
    start = timer()
    found = False
    movieList = []
    for key in movie:
        if titleType == movie[key].titleType:
            m = movie[key]
            if startYear == m.startYear and genre in m.genres:
                found = True
                movieList.append(movie[key])

    movieList.sort(key=operator.attrgetter('primaryTitle'))

    if not found:
        print("\tNo match found!")
    else:
        for m in movieList:
            print("\tIdentifier: ", m.tconst, ", Title: ", m.primaryTitle, ", Type: ", m.titleType,
                  ", Year: ", m.startYear, ", Runtime: ", m.runTime, ", Genres: ", m.genres)

    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")


