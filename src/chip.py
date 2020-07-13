''' 

COIN OBJECT FOR MANAGING PLAYING CHIPS

'''

class Chip:

    def __init__(self):
        self.total = 100 # starting amount

    def add(self, value):
        self.total += value

    def subtract(self, value):
        self.total -= value
    
    def add_multiple(self, value, multiple):
        value = value * multiple
        self.add(value)