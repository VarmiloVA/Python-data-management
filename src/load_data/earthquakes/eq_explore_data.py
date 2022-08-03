import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_1_day_m1.json'
with open(filename, 'r') as f:
    all_eq_data = json.load(f)

# Get a readable json from the original file
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

earthquakes = all_eq_data["features"]
mags, lons, lats, hover_texts = [], [], [], []
for earthquake in earthquakes:
    mag = earthquake["properties"]["mag"]
    lon = earthquake["geometry"]["coordinates"][0]
    lat = earthquake["geometry"]["coordinates"][1]
    title = earthquake["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Locates the earthquakes in a world map
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": hover_texts,
    "marker": {
        "size": [5 * mag for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {'title': 'Magnitude'}
}}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='graphs/global_earthquakes.html')