import random

class Thief:
    sneaky = True
    
    def __init__(self, name, sneaky=True, **kwargs):
        self.name = name
        self.sneaky = sneaky
        
        for key, value in kwargs.items():
            setattr(self, key, value)
                
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0,1))
    
    def hide(self, light_level):
        return self.sneaky and light_level < 10

# racecar.py challenge
# make the RaceCar class and initialize it with color, fuel_remaining
# and add the ability to take in more attributes    
class RaceCar:
    def __init__(self, color, fuel_remaining, laps = 0, **kwargs):
        self.color = color
        self.laps = laps
        self.fuel_remaining = fuel_remaining
        for key, value in kwargs.items():
            setattr(self,key,value)
            
    # add in a method called run_lap that takes a length, and reduces
    # the fuel_remaining by length multiplied by 0.125, also add a lap
    # attribute to the class (set to 0) that increments when run_lap is called
    def run_lap(self, length):
        self.laps += 1
        self.fuel_remaining -= (length * .125)
        