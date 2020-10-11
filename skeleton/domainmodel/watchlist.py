from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self._watchlist = []
        self._iterNum = 0

    def __iter__(self):
        self._iterNum = 0
        return self

    def __next__(self):
        if self._iterNum < len(self._watchlist):
            m = self._watchlist[self._iterNum]
            self._iterNum += 1
            return m
        else:
            raise StopIteration

    def add_movie(self, v):
        if v not in self._watchlist:
            self._watchlist.append(v)

    def remove_movie (self, v):
        if v in self._watchlist:
            self._watchlist.remove(v)

    def select_movie_to_watch(self, i):
        if i < len(self._watchlist) and i >= 0:
            return self._watchlist[i]
        else:
            return None

    def size(self):
        return len(self._watchlist)

    def first_movie_in_watchlist(self):
        if len(self._watchlist) == 0:
            return None
        else:
            return self._watchlist[0]



    @property
    def watchlist(self):
        return self._watchlist
    @watchlist.setter
    def watchlist(self, v):
        self._watchlist  = v


class TestWatchlistMethods:

    def test_init(self):
        watchlist = WatchList()
        print(f"Size of watchlist: {watchlist.size()}")
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print(watchlist.size())
        print(watchlist.first_movie_in_watchlist())

    def test_select(self):
        print("select testing:")
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print(watchlist.select_movie_to_watch(0))
        print(watchlist.select_movie_to_watch(1))
        print(watchlist.select_movie_to_watch(2))
        print(watchlist.select_movie_to_watch(3))
        print(watchlist.first_movie_in_watchlist())

    def test_delete(self):
        print("delete testing:")
        watchlist = WatchList()
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print(watchlist.select_movie_to_watch(0))
        watchlist.remove_movie(Movie("Ice Age", 2002))
        watchlist.remove_movie(Movie("Up", 2011))
        print(watchlist.first_movie_in_watchlist())

    def test_iter(self):
        print("iter testing: ")
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        for i in watchlist:
            print(i)



# These were used for testing
# t = TestWatchlistMethods()
# t.test_init()
# t.test_select()
# t.test_delete()
# t.test_iter()


#domainmodel.watchlist