from datetime import *

class Review:

    reviews = []

    def __init__(self, customer, restaurant, rating, content, date):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.date = date
        self.content = content
        self.reviews.append(self)

    def all():
        return Review.reviews
