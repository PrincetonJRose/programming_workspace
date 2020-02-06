from models.review import *

class Restaurant():

    restaurants = []

    def __init__(self, name):
        self.name = name.title()
        self.restaurants.append(self)

    def reviews(self):
        return list(map(lambda review: vars(review), list(filter(lambda review: review.restaurant == self, Review.reviews))))

    def all():
        return Restaurant.restaurants

    def find_by_name(name):
        return list(filter(lambda restaurant: restaurant.name == name.title(), Restaurant.all()))[0]
