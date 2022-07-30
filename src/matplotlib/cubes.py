from matplotlib.cm import ScalarMappable
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter

def visual(x_val, y_val):
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    #Generando los puntos
    if len(x_val) > 1000:
        ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.twilight_shifted, s=20)
    else:
        ax.scatter(x_val, y_val, c='Red', s=15)

    #Título del gráfico
    ax.set_title('Cube numbers', fontsize=24)
    #Etiquetas de los ejes
    ax.set_xlabel('Numbers', fontsize=14)
    ax.set_ylabel('Its cube', fontsize=14)
    #Quita la notación científica
    ax.ticklabel_format(style=('plain'))
    #Establece el tamaño de las etiquetas de los puntos de los ejes.
    ax.tick_params(axis='both', which='major', labelsize=14)

    #Rango de cada eje
    ax.set(xlim=(0, 5100), ylim=(0, 145000000000))

    #Guardando y mostrando gráfico
    plt.savefig('figs/cubes.png')
    plt.show()

if __name__ == '__main__':
    try:
        x_val = []
        y_val = []

        # Range 5
        # for i in range(5):
        #     x_val.append(i)
        #     y_val.append(i**3)

        # Range 5000
        for i in range(5000):
            x_val.append(i)
            y_val.append(i**3)
        
        visual(x_val, y_val)
    
    except KeyboardInterrupt:
        print('\nBye!\n')
