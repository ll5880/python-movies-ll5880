from timeit import default_timer as timer
import operator
from Class_Movie import Movie
from Class_Ratings import Ratings
from movies_main import main


def lookUp(tconst, movie, ratings) -> None:
    m = movie[tconst]
    r = ratings[tconst]
    if tconst in movie and tconst in ratings:
        print("Processing: LOOKUP ", tconst)
        start = timer()
        print("\tMOVIE: Identifier: ", m.tconst, ", Title: ", m.primaryTitle, ", Type: ",
              m.titleType, ", Year: ", m.startYear, ", Runtime: ", m.runTime, ", Genres: ", m.genres, "\n")
        print("\tRATING: Identifier: ", r.tconst, ", Rating: ", r.averageRating, ", Votes: ", r.numVotes)
        elapsed = timer() - start
        print('elapsed time (s):', elapsed)
    else:
        print("Processing: LOOKUP ", tconst)
        start = timer()
        print("\tMovie not found!")
        print("\tRating not found!")
        elapsed = timer() - start
        print('elapsed time (s):', elapsed)


def Contains(titleType, words, movie) -> None:
    print("\nprocessing: CONTAINS ", titleType, words)
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
        print("Not found!")
    else:
        for m in movieList:
            print("\tIdentifier: ", m.tconst, ", Title: ", m.primaryTitle, ", Type: ", m.titleType,
                  ", Year: ", m.startYear, ", Runtime: ", m.runTime, ", Genres: ", m.genres, "\n")

    elapsed = timer() - start
    print('elapsed time (s):', elapsed)


def Year_and_Genre(titleType, startYear, genre, movie) -> None:
    print("\nprocessing: Year_and_Genre ", titleType, startYear, genre)
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
        print("Not found!")
    else:
        for m in movieList:
            print("\tIdentifier: ", m.tconst, ", Title: ", m.primaryTitle, ", Type: ", m.titleType,
                  ", Year: ", m.startYear, ", Runtime: ", m.runTime, ", Genres: ", m.genres, "\n")

    elapsed = timer() - start
    print('elapsed time (s):', elapsed)


def RunTime (titleType, startTime, endTime, movie) -> None:
    print("\nprocessing: RUNTIME ", titleType, startTime, endTime)
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
        print("Not found!")
    else:
        for m in movieList:
            print("\tIdentifier: ", m.tconst, ", Title: ", m.primaryTitle, ", Type: ", m.titleType,
                  ", Year: ", m.startYear, ", Runtime: ", m.runTime, ", Genres: ", m.genres, "\n")

    elapsed = timer() - start
    print('elapsed time (s):', elapsed)

def Most_Votes(titleType, num, movie, ratings) -> None:
    print("\nprocessing: MOST_VOTES ", titleType, num)
    start = timer()
    movieList = []
    ratingList = []

    for key in ratings:
        if titleType == movie[key].titleType:
            ratingList.append(ratings[key])

    ratingList.sort(key=lambda  x: movie[x.tconst].primaryTitle)
    ratingList.sort(key=operator.attrgetter('numVotes'), reverse=True)

    for i in range(num):
        movieList.append(movie[ratingList[i].tconst])

    for movie in movieList:
        print(movie)

    elapsed = timer() - start
    print('\nelapsed time (s):', elapsed)

def Top(titleType, num, startYear, endYear, movie, ratings) -> None:
    print("\nprocessing: TOP ", titleType, num, startYear, endYear)
    start = timer()
    movieList = []
    for key in movie:
        if titleType == movie[key].titleType and startYear <= movie[key].startYear <= endYear:
            m = movie[key]
            movieList.append(movie[key])

    for movie in movieList:
        print(movie)

    elapsed = timer() - start
    print('\nelapsed time (s):', elapsed)


