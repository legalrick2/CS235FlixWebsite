
class Genre:
    
    def __init__(self, inigenreName: str):
        if inigenreName == "" or type(inigenreName) is not str:
            self._genreName = None
        else:
            self._genreName = inigenreName.strip()

    @property
    def genre_name(self) -> str:
        return self._genreName

    def __repr__(self):
        return f"<Genre {self._genreName}>"

    def __eq__(self, other):
        return (self.genre_name.lower() == other.genre_name.lower())

    def __lt__(self, other):
        return (self.genre_name < other.genre_name)

    def __hash__(self):
        return hash(self.genre_name)

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


#These were used for testing
# t = TestGenreMethods()
# t.testInit()
# t.testRepr()
# t.testEq()
# t.testLt()
# t.testHash()
