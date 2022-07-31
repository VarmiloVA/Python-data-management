import csv
import matplotlib.pyplot as plt
from datetime import date, datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # print("\n")
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    
    #DATE -> column 2 | TMAX -> column 5 | TMIN -> column 6
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(date)
            highs.append(int(row[5]))
            lows.append(int(row[6]))
        except ValueError:
            print(f"Missing data for {date}")
            dates.remove(date)

    # print("\n")
    # for i in range(len(highs)):
    #     print(date[i], "->", highs[i])   
    # print("\n")

#Plot the maximum temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 6), dpi=80)
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Da formato al trazado
plt.title('Daily temperatures | Death Valley, CA | 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F°)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()