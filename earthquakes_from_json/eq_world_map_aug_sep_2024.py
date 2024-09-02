import datetime
import json

from plotly import offline
from plotly.graph_objs import Layout

# Explore data structure
filename = 'data/eq_data_aug_sep_2024.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts, timestamps = [], [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    timestamp = eq_dict['properties']['time']

    if mag is not None and mag > 0:
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(title)
        timestamps.append(timestamp)

start_end_timestamps, dates = [min(timestamps), max(timestamps)], []
for timestamp in start_end_timestamps:
    timestamp_ms = timestamp
    timestamp_s = timestamp_ms / 1000
    date_time = datetime.datetime.utcfromtimestamp(timestamp_s)
    formatted_date = date_time.strftime('%m-%d-%Y')
    dates.append(formatted_date)

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title=f'Global Earthquakes for {dates[0]} - {dates[1]}')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
