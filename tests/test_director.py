import pytest

from skeleton.domainmodel.director import Director

@pytest.fixture
def director():
    return Director()


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