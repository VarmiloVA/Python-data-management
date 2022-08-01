import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(enumerate(header_row))

    dates, prcp = [], []
    for row in reader:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(date)
            prcp.append(float(row[3]))
        except ValueError:
            print(f"Missing data for {date}")
            dates.remove(date)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 6), dpi=95)
ax.plot(dates, prcp, c='blue')

plt.title('Daily Precipitation | Sitka, AK | 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation (in)', fontsize=16)
plt.tick_params(axis='y', which='major', labelsize=16)

plt.show()