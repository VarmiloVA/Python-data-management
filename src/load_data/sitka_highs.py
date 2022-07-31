import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    print("\n")
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    #DATE -> column 2 & TMAX -> column 5
    date, highs = [], []
    for row in reader:
        date.append(row[2])
        highs.append(int(row[5]))

    print("\n")
    for i in range(len(highs)):
        print(date[i], "->", highs[i])   
    print("\n")