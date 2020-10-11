
from skeleton.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
import skeleton.domainmodel
import random

repoInstance = None

class MemoryRepository():
    def __init__(self):
        filename = 'skeleton/datafiles/Data1000Movies.csv'
        self.movie_file_reader = MovieFileCSVReader(filename)
        self.movie_file_reader.read_csv_file()
        self.movie_file_reader.sortByTitle()

    def getRandomMovie(self):
        mov = None
        mov = random.choice(self.movie_file_reader.dataset_of_movies)
        return mov

    def getRandomMovieID(self):
        ID = random.randint(0, len(self.movie_file_reader.dataset_of_movies))
        return ID

    def getMovieSelection(self,startNum, endNum):
        return self.movie_file_reader.dataset_of_movies[startNum: endNum]

    def getAllMovies(self):
        return self.movie_file_reader.dataset_of_movies

    def getMovieWithID(self, ID):
        return self.movie_file_reader.dataset_of_movies[ID]

    def getMovieWithPerfectTitle(self, title, start=0):
        for m in self.movie_file_reader.dataset_of_movies[start:]:
            if title == m.title:
                return m

    def getMovieIDWithPerfectTitle(self, title, start=0):
        for iter, m in enumerate(self.movie_file_reader.dataset_of_movies[start:]):
            if title == m.title:
                return iter

    def getMoviesContainingStringTitle(self, words):
        foundMovies = []
        words.lower()
        for iter, m in enumerate(self.movie_file_reader.dataset_of_movies):
            if words in m.title.lower():
                foundMovies.append(m)
        return foundMovies

    def getTotalNumMovies(self):
        return len(self.movie_file_reader.dataset_of_movies)

    def getMoviesWithGenre(self, genreName):
        foundMovies = []
        genreFound = skeleton.domainmodel.genre.Genre(genreName)
        for iter, m in enumerate(self.movie_file_reader.dataset_of_movies):
            for mg in m.genres:
                if (genreFound == mg):
                    foundMovies.append(m)
                    break
        return foundMovies

    def getAllGenres(self):
        return self.movie_file_reader.dataset_of_genres