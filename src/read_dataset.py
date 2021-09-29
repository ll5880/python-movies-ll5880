import sys
from Class_Movie import Movie
from Class_Ratings import Ratings
from timeit import default_timer as timer


def read_data() -> tuple:
    movie = {}
    ratings = {}
    countm = 0
    countr = 0
    i = 0
    if len(sys.argv) == 2:
        # opens the small data set
        start = timer()
        print("reading data/small.basics.tsv into dict...")
        with open("data/small.basics.tsv", encoding="utf-8") as f:
            for line in f:
                x = line.strip().split("\t")
                if x[4] == "0":
                    countm += 1
                    tconst = x[0]
                    titleType = x[1]
                    primaryTitle = x[2]
                    if x[5] == "\\N":
                        startYear = 0
                    else:
                        startYear = int(x[5])
                    if x[6] == "\\N":
                        endYear = 0
                    else:
                        endYear = int(x[6])
                    if x[7] == "\\N":
                        runtime = 0
                    else:
                        runtime = int(x[7])
                    genres = x[8]
                    movie[tconst] = Movie(tconst, titleType, primaryTitle, startYear, endYear, runtime, genres.split(","))
        elapsed = timer() - start
        print('elapsed time (s):', elapsed, "\n")

        start = timer()
        print("reading data/small.ratings.tsv into dict...")
        with open("data/small.ratings.tsv", encoding="utf-8") as f:
            for line in f:
                x = line.strip().split("\t")
                if x[0] in movie:
                    countr += 1
                    tconst = x[0]
                    averageRating = float(x[1])
                    numVotes = int(x[2])
                    ratings[tconst] = Ratings(tconst, averageRating, numVotes)
        elapsed = timer() - start
        print('elapsed time (s):', elapsed)

        print("\nTotal movies: ", countm)
        print("Total ratings: ", countr, "\n")

    else:
        # opens the large data set
        start = timer()
        print("reading data/title.basics.tsv into dict...")
        with open("data/title.basics.tsv", encoding="utf-8") as f:
            for line in f:
                x = line.strip().split("\t")
                if x[4] == "0":
                    countm += 1
                    tconst = x[0]
                    titleType = x[1]
                    primaryTitle = x[2]
                    if x[5] == "\\N":
                        startYear = 0
                    else:
                        startYear = int(x[5])
                    if x[6] == "\\N":
                        endYear = 0
                    else:
                        endYear = int(x[6])
                    if x[7] == "\\N":
                        runtime = 0
                    else:
                        runtime = int(x[7])
                    genres = x[8]
                    movie[tconst] = Movie(tconst, titleType, primaryTitle, startYear, endYear, runtime, genres.split(","))
        elapsed = timer() - start
        print('elapsed time (s):', elapsed)

        start = timer()
        print("reading data/title.ratings.tsv into dict...")
        with open("data/title.ratings.tsv", encoding="utf-8") as f:
            for line in f:
                x = line.strip().split("\t")
                if x[0] in movie:
                    countr += 1
                    tconst = x[0]
                    averageRating = float(x[1])
                    numVotes = int(x[2])
                    ratings[tconst] = Ratings(tconst, averageRating, numVotes)
        elapsed = timer() - start
        print('elapsed time (s):', elapsed)

        print("\nTotal movies: ", countm)
        print("Total ratings: ", countr)

    return movie, ratings

