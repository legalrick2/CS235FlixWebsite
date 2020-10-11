import csv

from skeleton.domainmodel.movie import Movie
from skeleton.domainmodel.actor import Actor
from skeleton.domainmodel.genre import Genre
from skeleton.domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = set([])
        self.__dataset_of_directors = set([])
        self.__dataset_of_genres = set([])

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile: #i delete "datafiles/"+ before posting to coderunner, if this isnt here then my IDE, vscode, doesnt find it
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                if Movie(row['Title'],int(row['Year'])) not in self.__dataset_of_movies:
                    self.__dataset_of_movies.append(Movie(row['Title'], int(row['Year'])))
                #description = row['Description']

                self.__dataset_of_directors.add(Director(row['Director']))
                self.dataset_of_movies[-1].director = Director(row['Director'])
                self.dataset_of_movies[-1].description = row['Description']
                self.dataset_of_movies[-1].runtime = int(row['Runtime (Minutes)'])
                self.dataset_of_movies[-1].rating = float(row['Rating'])

                for g in row['Genre'].split(","):
                    self.__dataset_of_genres.add(Genre(g.strip()))
                    self.dataset_of_movies[-1].add_genre(Genre(g.strip()))

                for a in row['Actors'].split(","):
                    self.__dataset_of_actors.add(Actor(a.strip()))
                    self.dataset_of_movies[-1].add_actor(Actor(a.strip()))


                #print(f"Movie {index} with title: {title}, release year {release_year}")

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies
    # @dataset_of_movies.setter
    # def dataset_of_movies(self, li):
    #     self._dataset_of_movies = li

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors
    # @dataset_of_actors.setter
    # def dataset_of_actors(self, li):
    #     self._dataset_of_actors = li

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors
    # @dataset_of_directors.setter
    # def dataset_of_directors(self, li):
    #     self._dataset_of_directors = li

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres
    # @dataset_of_genres.setter
    # def dataset_of_genres(self, li):
    #     self._dataset_of_genres = li

    def sortByTitle(self):
        self.__dataset_of_movies = sorted(self.__dataset_of_movies)

	
	
	
# filename = 'Data1000Movies.csv'
# movie_file_reader = MovieFileCSVReader(filename)
# movie_file_reader.read_csv_file()

# print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
# print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
# print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
# print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')

# #print(movie_file_reader.dataset_of_genres)
# print(movie_file_reader.dataset_of_movies[1])
# print(movie_file_reader.dataset_of_movies[1].director)
# print(movie_file_reader.dataset_of_movies[1].description)
# print(movie_file_reader.dataset_of_movies[1].runtime)


#datafilereaders.movie_file_csv_reader