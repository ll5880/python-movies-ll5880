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


def RunTime(titleType, startTime, endTime, movie) -> None:
    print("processing: RUNTIME ", titleType, startTime, endTime)
    start = timer()
    found = False
    movieList = []
    for key in movie:
        if titleType == movie[key].titleType:
            m = movie[key]
            if startTime <= m.runTime <= endTime:
                found = True
                movieList.append(movie[key])

    # sort the list here
    # 1. sort primaryTitles in ascending order
    movieList.sort(key=operator.attrgetter('primaryTitle'))
    # 2. sort runtime in reverse order.
    movieList.sort(key=operator.attrgetter('runTime'), reverse=True)

    if not found:
        print("\tNo match found!")
    else:
        for m in movieList:
            print("\tIdentifier: ", m.tconst, ", Title: ", m.primaryTitle, ", Type: ", m.titleType,
                  ", Year: ", m.startYear, ", Runtime: ", m.runTime, ", Genres: ", m.genres)

    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")


def Most_Votes(titleType, num, movie, ratings) -> None:
    print("processing: MOST_VOTES ", titleType, num)
    start = timer()
    found = False
    movieList = []
    ratingList = []

    for key in ratings:
        if titleType == movie[key].titleType:
            ratingList.append(ratings[key])
            found = True

    if not found:
        print("\tNo match found!")
    else:
        ratingList.sort(key=lambda x: movie[x.tconst].primaryTitle)
        ratingList.sort(key=operator.attrgetter('numVotes'), reverse=True)
        """problem is that its not printing out (still processing a list if num is greater than the list)"""
        i = 0
        for r in ratingList:
            movieList.append(movie[r.tconst])
            i += 1
            if i >= num:
                break
        j = 1
        for movie in movieList:
            print("\t", str(j) + ". VOTES:", str(ratingList[j-1].numVotes) + ", MOVIE: Identifier:", movie.tconst,
                  ", Title:", movie.primaryTitle, ", Type: ", movie.titleType,", Year:", movie.startYear, ", Runtime:",
                  movie.runTime, ", Genres:", movie.genres)
            j += 1
    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")



