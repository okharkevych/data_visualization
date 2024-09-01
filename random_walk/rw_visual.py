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
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors='none',
        s=15
    )

    # Single out the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(
        rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100
    )

    # Hide the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Generate a new walk? (y/n): ')
    if keep_running == 'n':
        break
