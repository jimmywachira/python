import random

class Hat:
    def __init__(self):
        self.houses = ["c2","e3","f3","f4"]

    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)
    
hat = Hat()
hat.sort("jimmy")    