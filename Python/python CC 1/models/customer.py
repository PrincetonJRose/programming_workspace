from models.review import *

class Customer():

    customers = []
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.customers.append(self)

    def reviews(self):
        return list(map(lambda review: vars(review), list(filter(lambda review: review.customer == self, Review.all()))))

    def all():
        return Customer.customers

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def find_by_name(name):
        return list(filter(lambda customer: customer.full_name() == name.title(), Customer.all()))[0]

    def find_all_by_first_name(name):
        return list(filter(lambda customer: customer.first_name == name.title(), Customer.all()))
    
    def all_names():
        return list(map(lambda customer: customer.full_name(), Customer.all()))

    def num_reviews(self):
        return len(self.reviews())

    def restaurants(self):
        my_reviews = list(filter(lambda review: review.customer == self, Review.all()))
        restaurants = list(set(map(lambda review: review.restaurant, my_reviews)))
        return restaurants
