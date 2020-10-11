from skeleton.domainmodel.genre import Genre
from skeleton.domainmodel.actor import Actor
from skeleton.domainmodel.director import Director

class Movie:
    def __init__(self, title : str, year : int):
        if title == "" or type(title) is not str:
            self._title  = None
        else:
            self._title  = title.strip()
        
        if year < 1900 or type(year) is not int:
            self._year = None
        else:
            self._year = year
        
        self._description = ""
        self._director = Director("")
        self._actors = []
        self._genres = []
        self._runtime_minutes = 0
        self._rating = 0

    

    def __repr__(self):
        return f"<Movie {self.title}, {self.year}>"

    def __eq__(self, other):
        return (self.title.lower() == other.title.lower() and self.year == other.year)

    def __lt__(self, other):
        if self.title == other.title:
            return (self.year < other.year)
        else:
            return (self.title < other.title)

    def __hash__(self):
        return (hash((self.title, self.year)))

    def add_actor(self, actor):
        self._actors.append(actor)

    def remove_actor(self, actor):
        if actor in self._actors:
            self._actors.remove(actor)

    def add_genre(self, genre):
        self._genres.append(genre)

    def remove_genre(self, genre):
        if genre in self._genres:
            self._genres.remove(genre)


    @property
    def title(self) -> str:
        return self._title
    @title.setter
    def title(self, val):
        self._title = val.strip()

    @property
    def year(self) -> int:
        return self._year
    @year.setter
    def year(self, val):
        if (val < 1900):
            self._year = None
        else:
            self._year = val

    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, desc):
        self._description = desc.strip()

    @property
    def director(self):
        return self._director
    @director.setter
    def director(self, direc):
        if type(direc) is Director:
            self._director = direc
        
    @property
    def actors(self) -> []:
        return self._actors
    @actors.setter
    def actors(self, li):
        self._actors = li

    @property
    def genres(self) -> []:
        return self._genres
    @genres.setter
    def genres(self, li):
        self._genres = li
    
    @property
    def runtime_minutes(self) -> int:
        return self._runtime_minutes
    @runtime_minutes.setter
    def runtime_minutes(self, time):
        if (time > 0):
            self._runtime_minutes = time
        else:
            raise(ValueError)

    @property
    def rating(self) -> int:
        return self._rating
    @rating.setter
    def rating(self, val):
        if (val >= 0 and val <= 10):
            self._rating = val
        else:
            raise(ValueError)

    # @property
    # def id(self) -> int:
    #     return self._id
    # @id.setter
    # def id(self, val):
    #     self._id
        

    # def __eq__(self, other):
    #     return (self.actor_full_name.lower() == other.actor_full_name.lower())

    # def __lt__(self, other):
    #     return (self.actor_full_name.lower() < other.actor_full_name.lower())

    # def __hash__(self):
    #     return hash(self.actor_full_name)

    # @property
    # def apple():
    # return __apple

    # @apple.setter
    # def apple(food):
    # apple = food


class TestMovieMethods:
    def testInit(self):
        print("init test: ")
        movie1 = Movie("   Moana     ", 2016)
        movie2 = Movie("Clam Wars", 1200)
        movie3 = Movie("", 1200)
        print((movie1.year == 2016 )is True)
        print((movie1.title == "Moana")is True)
        print((movie2.year == None) is True)
        print((movie2.title == "Clam Wars") is True)
        print((movie3.title == None and movie3.year == None) is True)

    def testRepr(self):
        print("repr test: ")
        movie1 = Movie("Moana", 2016)
        print(movie1)

    def testEq(self):
        print("eq test: ")
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Up", 2009)
        movie3 = Movie("Up", 2002)
        movie4 = Movie("Up", 2009)
        print((movie1 == movie2) is False)
        print((movie2 == movie3) is False)
        print((movie2 == movie4) is True)

    def testLt(self):
        print("lt test: ")
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Up", 2009)
        movie3 = Movie("Up", 2002)
        print((movie1 < movie2)is True)
        print((movie2 < movie3) is False)
        print((movie1 < movie3) is True)

    def testHash(self):
        print("Hash test: ")
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Up", 2009)
        movie3 = Movie("Moana", 2016)
        print(hash(movie1))
        print(hash(movie3))
        print(hash(movie2))

    def testGenres(self):
        print("Genre testing:")
        movie1 = Movie("Moana", 2016)
        movie1.add_genre(Genre("Cheesy"))
        movie1.add_genre(Genre("Action"))
        movie1.remove_genre(Genre("Cheesy"))
        print(movie1.genres)

    def testDirector(self):
        print("Director testing:")
        movie1 = Movie("Moana", 2016)
        movie1.director = 9 #Director("Meee")
        print(movie1.director)

    def descTest(self):
        print("Desc test:")
        movie1 = Movie("Moana", 2016)
        movie1.description = "   Well something happens   "
        print(movie1.description)


# movie = Movie("Moana", 2016)
# print(movie)

# director = Director("Ron Clements")
# movie.director = director
# print(movie.director)

# actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
# for actor in actors:
#     movie.add_actor(actor)
# print(movie.actors)

# movie.runtime_minutes = 107
# print("Movie runtime: {} minutes".format(movie.runtime_minutes))

# myMovie = Movie("Rat King 3 ", 2010)
# print(myMovie)
# myMovie.description = "In a world where...   "
# myMovie.actors = [Actor("Beefy grill")]
# myMovie.add_actor(Actor("Ratty boi"))
# myMovie.add_actor(Actor("Ratty ww"))
# myMovie.remove_actor(Actor("Ratty ww"))
# myMovie.remove_actor(Actor("AH"))
# myMovie.add_genre(Genre("Action"))
# myMovie.add_genre(Genre("Cheese"))
# myMovie.remove_genre(Genre("Cheese"))
# myMovie.director = Director("Jim Stacy")
# myMovie.runtime_minutes = 67
# print(myMovie)
# print(myMovie.actors)
# print(myMovie.genres)
# print(myMovie.description)
# print(myMovie.year)
# print(myMovie.director)
# print(myMovie < movie)
# print(myMovie == movie)


# # These were used for testing
# t = TestMovieMethods()
# t.testInit()
# t.testRepr()
# t.testEq()
# t.testLt()
# t.testHash()
# t.testGenres()
# t.testDirector()
# t.descTest()