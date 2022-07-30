import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    """Una clase para generar caminos aleatorios"""
    def __init__(self, num_points):
        self.num_points = num_points

        #Todos los caminos empiezan en (0, 0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calcula todos los puntos de un camino"""

        #Sigue dando pasos hasta que el camino alcanza la longitud deseada.
        while len(self.x_values) < self.num_points:
            #Decide en que dirección ir y cuánto avanzar en esa dirección.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Rechaza movimientos que no van a ninguna parte.
            if x_step == 0 and y_step == 0:
                continue

            #Calcula la nueva posición.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

if __name__ == '__main__':
    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()

        #Trazar los puntos del camino
        plt.style.use('classic')
        fig, ax = plt.subplots()
        ax.scatter(rw.x_values, rw.y_values, c='red', s=15)
    
        plt.show()

        #¿Hacer otro camino?
        keep_running = input("Make another walk? (y/n): ")
        if keep_running.lower() == 'n':
            break