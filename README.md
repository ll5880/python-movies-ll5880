# Movie Dictionary in Python

## Description
This project includes a dictionary of movies & ratings and depending on the input commands it 
reads from an input file, it will perform that specific search and time
the duration of execution. There are several commands to tests, and various different input files 
with varying commands and sizes of data used for them.

The commands are Lookup, Contains, Year_And_Genre, Runtime, Most_Votes, and Top. 

Depending on the type of Command, the input for that command will request 
certain arguments. 

The project utilizes dictionaries in python in order to understand and test the
functionalities of them.

## Commands
Lookup ( tconstant, movie, rating ) - a tconstant is a unique number identifier for each
movie and their rating. The lookup command will take in the given tconstant
and search through the dataset of movies and ratings and provide information
about that movie and its associated rating. 

Contains ( titletype, titlestr, movie ) - The command will search through the database
of movies and find movies that match the titletype and then check if the title
of that movie contains the titlestr. The command will provide a list of movies
that contains the titlestr and match the titletype

Year_And_Genre ( titletype, startyear, genre, movie ) - The command will search through
the database of movies and provide a list of movies that fit the genre, the start 
year, and title type. 

Runtime ( titletype, starttime, endtime, movie ) - will provide a list of movies that 
match the titletype and the runtime of the movie is within the startime and 
endtime

Most_Votes ( titletype, num , movie, ratings ) - provides a list of num amount of movies, that
match the titletype. The list of movies that fit this category are then sorted
alphabetically first and then sorts the movies in descending order by ratings

Top ( titleType, num, startYear, endYear, movie, ratings ) - provides a list of num
amount of movies of a certain format, within a certain time frame, that have over 
1000 votes and are the highest rated.

## Challenges

Some challenges behind the project was sorting the list of movies found, in an
efficient manner. There were thoughts of sorting it using foreach statements
however it would be tedious to sort through each list. However python has a 
built in sort() function which makes this process easier by sorting the list
with provided arguments and the list can be reversed with a simple true or false.






