import json
from plotly.graph_objs import Bar, Layout
from plotly import offline

filename = 'data/eq_data_1_day_m1.json'
with open(filename, 'r') as f:
    all_eq_data = json.load(f)

# Get a readable json from the original file
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

metadata = all_eq_data["metadata"]
earthquakes = all_eq_data["features"]
mags_recorded = []
locations_recorded = []
for earthquake in earthquakes:
    properties = earthquake["properties"]
    mags_recorded.append(properties["mag"])
    locations_recorded.append(properties["place"])

# sorted_mags = sorted(mags_recorded)
data = [Bar(x=locations_recorded, y=mags_recorded)]
x_axis_config = {'title': 'Locations'}
y_axis_config = {'title': 'Magnitude', 'dtick': 0.3}
my_layout = Layout(title=str(metadata["title"]), xaxis=x_axis_config,
    yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='graphs/earthquakes.html')
