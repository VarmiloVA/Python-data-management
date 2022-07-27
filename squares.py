import matplotlib.pyplot as plt
import psycopg2
from numpy import square

def connect_database():
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres",
                                password="mondayl#tm#brok#n", host="localhost", port="5433")
        conn.set_session(autocommit=True)
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

def execute(conn, query, *params):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()

def save_data(conn):
    try:
        cursor = conn.cursor()
        query_save_data = '''INSERT INTO squares(number, square) VALUES (%s, %s)'''
        for i in range(0, 1000):
            cursor.execute(conn, query_save_data, (i, int(square(i))))
            conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally: # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection has been closed")
    
def _get_data(conn):
    try:
        cursor = conn.cursor()
        query = '''SELECT number, square FROM squares'''
        cursor.execute(query)

        x_values = []
        y_values = []
        for record in cursor.fetchall():
            x, y = record
            x_values.append(x)
            y_values.append(y)
        return x_values, y_values

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally: # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection has been closed")

def delete_data(conn):
    cursor = conn.cursor()
    query = '''DELETE FROM squares WHERE number=%s'''

    for i in range(0, 1000):
        cursor.execute(conn, query, [i])
        conn.commit()

    cursor.close()
    print('Data succesfully deleted')

def visual(**kwargs):
    if 'x_val' in kwargs and 'y_val' in kwargs:
        x_values = kwargs['x_val']
        y_values = kwargs['y_val']

    else:       
        x_values = []
        y_values = []
        for i in range(0, 100):
            x_values.append(i)
            y_values.append(square(i))

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c='blue', s=10)

    ax.plot(x_values, y_values, linewidth=2)

    #Establece el título del gráfico y las etiquetas de los ejes.
    ax.set_title('Square Numbers', fontsize=24)
    ax.set_xlabel('Value', fontsize=14)
    ax.set_ylabel('Square of Value', fontsize=14)
    #Quita la notación científica
    ax.ticklabel_format(style=('plain'))

    #Establece el tamaño de las etiquetas de los puntos de los ejes.
    ax.tick_params(axis='both', which='major', labelsize=14)

    #Establece el rango de cada eje.
    ax.set(xlim=(0,11), ylim=(0,110))

    plt.show()

conn = connect_database()
while True:
    user_entry = input('\nWhat do you want to do?\n1. Save data\n2. Delete data\n3. Visualize data\n4. Exit\n\n--> ')
    if user_entry == '1':
        save_data(conn)
    elif user_entry == '2':
        delete_data(conn)
    elif user_entry == '3':
        x_val, y_val = _get_data(conn)
        visual(x_val=x_val, y_val=y_val)
    elif user_entry == '4':
        break