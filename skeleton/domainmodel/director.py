
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        return (self.director_full_name.lower() == other.director_full_name.lower())

    def __lt__(self, other):
        return (self.director_full_name < other.director_full_name)

    def __hash__(self):
        return hash(self.director_full_name)


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None

    def testRepr(self):
        director1 = Director("Taika Waititi")
        print(director1)
        print("Hello "+ director1.director_full_name)

    def testEq(self):
        print("= Testing:")
        director1 = Director("Tom Scott")
        director2 = Director("tom scott")
        director3 = Director("James Bond")
        director4 = Director("james Bond")
        print((director1 == director2 )is True)
        print((director3 == director4 )is True)
        print((director1 == director3 )is False)
        print((director4 == director2) is False)

    def testLt(self):
        print("< Testing:")
        director1 = Director("Abe Scott")
        director2 = Director("abe scott")
        director3 = Director("Bess Bond")
        print((director1 < director2) is False)
        print((director1 < director3) is True)
        print((director3 < director1) is False)

    def testHash(self):
        print("Hash Testing:")
        director1 = Director("Tom Scott")
        tomDict = {"Director": director1, "Movies": 6, "Food": "Meat"}
        print(tomDict.get("Director"))
        print(tomDict.get("Food"))
        print(tomDict["Movies"])



# These were used for testing
# t = TestDirectorMethods()
# t.test_init()
# t.testRepr()
# t.testEq()
# t.testLt()
# t.testHash()
