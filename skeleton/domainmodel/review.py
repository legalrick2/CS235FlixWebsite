from datetime import datetime

from skeleton.domainmodel.movie import Movie

class Review:

    def __init__(self,inimovie,initext,inirating):
        if inirating >= 1 and inirating <= 10:
            self._rating = inirating
        else:
            self._rating = None


        self._movie = inimovie
        self._review_text = initext
        
        self._timestamp = datetime.now()

    def __repr__(self):
        return f"{self.movie} {self.review_text} {self.rating}/10"

    def __eq__(self,other):
        return (self.timestamp == other.timestamp) and (self.rating == other.rating) and (self.moive == other.movie) and (self.review_text == other.review_text)

    @property
    def movie(self):
        return self._movie
    @movie.setter
    def movie(self, v):
        self._movie = v

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, v):
        if v >= 1 and v <= 10:
            self._rating = v
        else:
            self._rating = None

    @property
    def review_text(self):
        return self._review_text
    @review_text.setter
    def review_text(self, v):
        self._review_text = v

    @property
    def timestamp(self):
        return self._timestamp
    
# movie = Movie("Moana", 2016)
# review_text = "This movie was very enjoyable."
# rating = 8
# review = Review(movie, review_text, rating)

# print(review.movie)
# print("Review: {}".format(review.review_text))
# print("Rating: {}".format(review.rating))
# print(review.timestamp)
# print(review)


#domainmodel.review