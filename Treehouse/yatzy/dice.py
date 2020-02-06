import random

class Die:
	def __init__(self, sides = 4, value = 0):
		if not sides >= 4:
			raise ValueError("Must have at least 4 sides")
		if not isinstance(sides, int):
			raise ValueError("Sides must be a whole number")
		if not isinstance(value, int):
			raise ValueError("Value must be a whole number")
		self.value = value or random.randint(1, sides)
		
	def __int__(self):
		return self.value
	
	def __eq__(self, other):
		return int(self) == other
	
	def __ne__(self, other):
		return int(self) != other
	
	def __gt__(self, other):
		return int(self) > other
	
	def __lt__(self, other):
		return int(self) < other
	
	def __ge__(self, other):
		return int(self) >= other
	
	def __le__(self, other):
		return int(self) <= other

	def __add__(self, other):
		return int(self) + other
	
	def __radd__(self, other):
		return int(self) + other
		
class D6(Die):
	def __init__(self, value = 0):
		super().__init__(sides = 6, value = value)

class D8(Die):
	def __init__(self, value = 0):
		super().__init__(sides = 8, value = value)

class D10(Die):
	def __init__(self, value = 0):
		super().__init__(sides = 10, value = value)
	
class D20(Die):
	def __init__(self, value = 0):
		super().__init__(sides = 20, value = value)

