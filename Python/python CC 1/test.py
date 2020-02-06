import os
import sys
import pry
import unittest
from mamba import *
from expects import *

from models.review import *
from models.customer import *
from models.restaurant import *

p = Customer('Princeton', 'Rose')
m = Customer('Maddie', 'Ward')
rest1 = Restaurant('Chick-fil-A')
rest2 = Restaurant('Burger King')
rest3 = Restaurant("McDonald's")
r1 = Review(p, rest2, 4, 'Cheap burgers at an okay price. Nothing special...', datetime.now())
r2 = Review(m, rest1, 0, 'This company is the worst absolute garbage on the planet!', datetime.now())
r3 = Review(m, rest1, 0, 'This company is full of haters!', datetime.now())
r3 = Review(m, rest2, 3, 'Mediocrity is this places motto.', datetime.now())
print(Review.reviews[0])
pry()