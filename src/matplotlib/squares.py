import matplotlib.pyplot as plt
from numpy import square

def visual(x_val, y_val):
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    #Generar línea con los valores de x y sus cuadrados.
    ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Blues, s=10)
    #Mostrar los puntos de los valores x y sus cuadrados.
    #ax.plot(values['x_val'], values['y_val'], linewidth=2)

    #Establece el título del gráfico y las etiquetas de los ejes.
    ax.set_title('Square Numbers', fontsize=24)
    ax.set_xlabel('Value', fontsize=14)
    ax.set_ylabel('Square of Value', fontsize=14)
    #Quita la notación científica
    ax.ticklabel_format(style=('plain'))

    #Establece el tamaño de las etiquetas de los puntos de los ejes.
    ax.tick_params(axis='both', which='major', labelsize=14)

    #Establece el rango de cada eje.
    ax.set(xlim=(0,1100), ylim=(0,1100000))

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