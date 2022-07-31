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
            #Se recoge la dirección y longitud de los pasos.
            x_step, y_step = self._get_step()
            #Rechaza movimientos que no van a ninguna parte.
            if x_step == 0 and y_step == 0:
                continue

            #Calcula la nueva posición.
            x = self.x_values[-1] + x_step

            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    def _get_step(self):
        #Decide en que dirección ir y cuánto avanzar en esa dirección.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance
            return x_step, y_step

if __name__ == '__main__':
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #Trazar los puntos del camino
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(9, 6), dpi=128)
    ax.scatter(rw.x_values, rw.y_values, c='blue', s=1, edgecolors='none')
    ax.scatter(rw.x_values[0], rw.y_values[0], c='black', s=40, edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=40, edgecolors='none')

    #Ocultar los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()                                                                  