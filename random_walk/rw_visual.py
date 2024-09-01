import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Generate new walks while the program is active
while True:
    # Generate random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Record random walk points on the graph
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)

    plt.show()

    keep_running = input('Generate a new walk? (y/n): ')
    if keep_running == 'n':
        break
       