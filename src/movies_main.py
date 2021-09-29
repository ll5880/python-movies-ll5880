import sys
from process_queries import*
from read_dataset import read_data


def main():
    movie, ratings = read_data()

    for line in sys.stdin:
        l = line.strip().split(" ")
        if l[0][0:1] == "L":
            lookUp(l[1], movie, ratings)
        elif l[0][0:1] == "C":
            words = ""
            i = 2
            while i < len(l):
                words += l[i]
                i += 1
            Contains(l[1], words, movie)
            """problems: you did not format the words right (no spaces) but if you add spaces then you will get an extra
            space at the end of a word and that throws off the results"""
        elif l[0][0:1] == "Y":
            Year_and_Genre(l[1], int(l[2]), l[3], movie)
        elif l[0][0:1] == "R":
            RunTime(l[1], int(l[2]), int(l[3]), movie)
        elif l[0][0:1] == "M":
            Most_Votes((l[1]), int(l[2]), movie, ratings)
        else:
            Top(l[1], int(l[2]), int(l[3]), int(l[4]), movie, ratings)

if __name__ == '__main__':
    main()

