import pytest

from skeleton.domainmodel.genre import Genre

@pytest.fixture
def genre():
    return Genre()

class TestGenreMethods:
    def testInit(self):
        genre1 = Genre("Horror")
        print(genre1.genre_name == "Horror")
        genre2 = Genre("")
        print(genre2.genre_name == None)
        genre3 = Genre(42)
        print(genre3.genre_name == None)
        
    def testRepr(self):
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        print(genre1)
        print("The genre is "+ genre2.genre_name)

    def testEq(self):
        print("= Testing:")
        genre1 = Genre("Horror")
        genre2 = Genre("Comedy")
        genre3 = Genre("HORROR")
        print((genre1 == genre2) is False)
        print((genre1 == genre3) is True)

    def testLt(self):
        print("< Testing:")
        genre1 = Genre("Action")
        genre2 = Genre("Horror")
        print((genre1 < genre2) is True)
        print((genre2 < genre1) is False)


    def testHash(self):
        pass