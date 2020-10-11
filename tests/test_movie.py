import pytest

from skeleton.domainmodel.movie import Movie
from skeleton.domainmodel.genre import Genre

@pytest.fixture
def movie():
    return Movie()

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
