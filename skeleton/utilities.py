
# from skeleton.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
# import random

# class Repository():
#     def __init__(self):
#         filename = 'skeleton/datafiles/Data1000Movies.csv'
#         self.movie_file_reader = MovieFileCSVReader(filename)
#         self.movie_file_reader.read_csv_file()
#         self.currentPlace = 0

#     def getRandomMovie(self):
#         mov = None
#         mov = random.choice(self.movie_file_reader.dataset_of_movies)
#         return mov

#     def getRandomMovieID(self):
#         ID = random.randint(0, len(self.movie_file_reader.dataset_of_movies))
#         return ID

#     def getMovieSelection(self,num):
#         return self.movie_file_reader.dataset_of_movies[self.currentPlace: num]

#     def increaseCurrentPlace(self, num):
#         self.currentPlace += num

#     def getAllMovies(self):
#         return self.movie_file_reader.dataset_of_movies

#     def getMovieWithID(self, ID):
#         return self.movie_file_reader.dataset_of_movies[ID]