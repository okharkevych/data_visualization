from random import randint


class Die:
    """Class represents one die"""

    def __init__(self, num_sides=6):
        """Define a die with 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value from 1 to 6"""
        return randint(1, self.num_sides)
