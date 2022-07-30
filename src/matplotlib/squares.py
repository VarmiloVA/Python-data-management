import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter
from numpy import square

def visual(x_val, y_val):
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    #Generar puntos con los valores de x y sus cuadrados.
    ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.twilight_shifted, s=10)
    #Mostrar los línea de los valores x y sus cuadrados.
    #ax.plot(values['x_val'], values['y_val'], linewidth=2)

    #Establece el título del gráfico y las etiquetas de los ejes.
    ax.set_title('Square Numbers', fontsize=24)
    ax.set_xlabel('Value', fontsize=14)
    ax.set_ylabel('Square of Value', fontsize=14)
    #Quita la notación científica
    ax.ticklabel_format(style=('plain'))

    ax.xaxis.set_minor_locator(MultipleLocator(100))
    ax.xaxis.set_minor_formatter(ScalarFormatter())

    #Establece el tamaño de las etiquetas de los puntos de los ejes.
    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.tick_params(axis='x', which='minor', labelsize=8)

    #Establece el rango de cada eje.
    ax.set(xlim=(0,1_100), ylim=(0,1_100_000))

    plt.savefig('figs/squares.png', bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    try:
        x_val = []
        y_val = []
    
        for i in range(1000):
            x_val.append(i)
            y_val.append(square(i))

        visual(x_val, y_val)

    except KeyboardInterrupt:
        print('\n\tBye!\n')