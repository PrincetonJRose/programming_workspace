import sys
import math
import random
import string
import time
import csv
import os
import copy

class FilledList(list):
	def __init__(self, count, value, *args, **kwargs):
		super().__init__()
		for _ in range(count):
			self.append(copy.copy(value))
			
class Liar(list):
    def __len__(self):
        return super(Liar, self).__len__() + 2
