import plotly
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        """Return a random value between 1 and die's number of sides."""
        return randint(1, self.sides)

if __name__ == '__main__':
    #Create a D6
    die = Die()

    results = []
    for roll_num in range(1000):
        results.append(die.roll())

    print(results)