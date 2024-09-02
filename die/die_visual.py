from plotly import offline
from plotly.graph_objs import Bar, Layout

from die import Die

# Create D6
die = Die()

# Make several rolls and save the results to a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, die.num_sides))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config,
    yaxis=y_axis_config
)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
