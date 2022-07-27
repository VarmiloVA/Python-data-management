import matplotlib.pyplot as plt
from numpy import square

values = {
    'x_val': [],
    'y_val': []
    }

for i in range(100):
    values['x_val'].append(i)
    values['y_val'].append(square(i))

def visual():
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(values['x_val'], values['y_val'], c='blue', s=10)

    ax.plot(values['x_val'], values['y_val'], linewidth=2)

    #Establece el título del gráfico y las etiquetas de los ejes.
    ax.set_title('Square Numbers', fontsize=24)
    ax.set_xlabel('Value', fontsize=14)
    ax.set_ylabel('Square of Value', fontsize=14)
    #Quita la notación científica
    ax.ticklabel_format(style=('plain'))

    #Establece el tamaño de las etiquetas de los puntos de los ejes.
    ax.tick_params(axis='both', which='major', labelsize=14)

    #Establece el rango de cada eje.
    ax.set(xlim=(0,110), ylim=(0,11000))

    plt.show()

if __name__ == '__main__':
    visual()