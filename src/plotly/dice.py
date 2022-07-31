from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint

from die import Die

if __name__ == '__main__':
    #Create a D6
    die_1 = Die(7)
    die_2 = Die(14)

    #Rolling the die and booking the results
    results = []
    for roll_num in range(1000):
        results.append(die_1.roll()+die_2.roll())

    #Analizing the results
    frequencies = []
    max_result = die_1.sides+die_2.sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    
    #Visualizing the results
    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]
    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layour = Layout(title=str(f'Results of rolling a D{die_1.sides} and a D{die_2.sides} 1000 times'),
        xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layour}, filename=str(f'd{die_1.sides}_d{die_2.sides}.html'))