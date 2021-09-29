import sys
from process_queries import*
from read_dataset import read_data


def main():

    # for line in sys.stdin:
    #      line is guaranteed to not be empty
    #     line.split()

    movie, ratings = read_data()
    # lookUp("tt0081505", movie, ratings)
    # lookUp("tt0816692", movie, ratings)
    # Contains("movie", "Avengers", movie)
    # Year_and_Genre("movie", 1995, "Action", movie)
    # RunTime("movie", 142, 168, movie)
    # Most_Votes("movie", 5, movie, ratings)
    Top("movie", 3, 1994, 1995, movie, ratings)


if __name__ == '__main__':
    main()

