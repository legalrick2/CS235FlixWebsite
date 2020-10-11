
class Actor:

    def __init__(self, actor_full_name : str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name  = None
        else:
            self.__actor_full_name  = actor_full_name.strip()
        self.colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return (self.actor_full_name.lower() == other.actor_full_name.lower())

    def __lt__(self, other):
        return (self.actor_full_name < other.actor_full_name)

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague):
        self.colleagues.append(colleague)
        colleague.colleagues.append(self)

    def check_if_this_actor_worked_with(self, colleague):
        return (self.colleagues.__contains__(colleague))

class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Actor Angelina Jolie>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(42)
        assert actor3.actor_full_name is None

    def testRepr(self):
        actor1 = Actor("Angelina Jolie")
        print(actor1)
        print("Hello "+ actor1.actor_full_name)

    def testEq(self):
        print("= Testing:")
        actor1 = Actor("Tom Scott")
        actor2 = Actor("tom scott")
        actor3 = Actor("James Bond")
        actor4 = Actor("james Bond")
        print((actor1 == actor2 )is True)
        print((actor3 == actor4 )is True)
        print((actor1 == actor3 )is False)
        print((actor4 == actor2) is False)

    def testLt(self):
        print("< Testing:")
        actor1 = Actor("Abe Scott")
        actor2 = Actor("abe scott")
        actor3 = Actor("Bess Bond")
        print((actor1 < actor2) is False)
        print((actor1 < actor3) is True)
        print((actor3 < actor1) is False)

    def testHash(self):
        print("Hash Testing:")
        actor1 = Actor("Tom Scott")
        tomDict = {"Actor": actor1, "Movies": 6, "Food": "Meat"}
        print(tomDict.get("Actor"))
        print(tomDict.get("Food"))
        print(tomDict["Movies"])

    def testColleagues(self):
        actor1 = Actor("Tom Scott")
        actor2 = Actor("James Bond")
        print(actor1.check_if_this_actor_worked_with(actor2) is False)
        print(actor2.check_if_this_actor_worked_with(actor1) is False)
        actor1.add_actor_colleague(actor2)
        print(actor1.check_if_this_actor_worked_with(actor2) is True)
        print(actor2.check_if_this_actor_worked_with(actor1) is True)

# These were used for testing
# t = TestActorMethods()
# t.test_init()
# t.testRepr()
# t.testEq()
# t.testLt()
# t.testHash()
# t.testColleagues()