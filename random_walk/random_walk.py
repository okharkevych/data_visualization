from random import choice


class RandomWalk:
    """Class that generates randow walk"""

    def __init__(self, num_points=5000):
        """Initiate walk attributes"""
        self.num_points = num_points

        # All walks start from (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # Decide on movement direction and distance
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step

    def fill_walk(self):
        """Calculate all walk points"""
        # Continue making steps until the walk reaches the needed length
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Discard steps that don't move anywhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
