from skeleton.domainmodel.movie import Movie
from skeleton.domainmodel.review import Review

class User:
    def __init__(self,iniusername,inipassword):

        self._user_name = iniusername.strip().lower()
        self._password = inipassword
        self._watched_movies = []
        self._reviews = []
        self._time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return f"<User {self.user_name}>"

    def __eq__(self, other):
        return (self.user_name == other.user_name)

    def __lt__(self, other):
        return (self.user_name < other.user_name)

    def __hash__(self):
        return hash((self.user_name, self.password))

    def watch_movie(self,movie):
        self._watched_movies.append(movie)
        self._time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self,review):
        self._reviews.append(review)


    @property
    def user_name(self):
        return self._user_name
    @user_name.setter
    def user_name(self, v):
        self._user_name = v.strip().lower()

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, v):
        self._password  = v

    @property
    def watched_movies(self):
        return self._watched_movies
    @watched_movies.setter
    def watched_movies(self, v):
        self._watched_movies  = v

    @property 
    def reviews(self):
        return self._reviews
    @reviews.setter
    def reviews(self, v):
        self._reviews  = v

    @property
    def time_spent_watching_movies_minutes(self):
        return self._time_spent_watching_movies_minutes
    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, v):
        if v > 0:
            self._time_spent_watching_movies_minutes = v


# user1 = User('Martin', 'pw12345')
# user2 = User('Ian', 'pw67890')
# user3 = User('Daniel', 'pw87465')
# print(user1)
# print(user2)
# print(user3)

# assert(user1 == user2)

#domainmodel.user