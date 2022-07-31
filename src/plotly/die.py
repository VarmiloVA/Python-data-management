from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        """Return a random value between 1 and die's number of sides."""
        return randint(1, self.sides)

if __name__ == '__main__':
    #Create a D6
    die = Die()

    #Rolling the die and booking the results
    results = []
    for roll_num in range(1000):
        results.append(die.roll())

    #Analizing the results
    frequencies = []
    for value in range(1, die.sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    
    #Visualizing the results
    x_values = list(range(1, die.sides+1))
    data = [Bar(x=x_values, y=frequencies)]
    x_axis_config = {'title': 'Result'}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layour = Layout(title=str(f'Results of rolling a D{die.sides} 1000 times'),
        xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layour}, filename=str(f'd{die.sides}.html'))