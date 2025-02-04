import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set graph and axes titles
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set font size for graph markings
ax.tick_params(axis='both', which='major', labelsize=14)

# Set range for each axis
ax.axis([0, 1100, 0, 1100000])

# use plt.savefig() instead to save to file
plt.show()
