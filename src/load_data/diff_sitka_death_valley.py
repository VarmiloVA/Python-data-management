import csv
import matplotlib.pyplot as plt
from datetime import date, datetime

#Death Valley data part
death_valley_data = 'data/death_valley_2018_simple.csv'
with open(death_valley_data) as f:
    reader_dv = csv.reader(f) # dv for death valley
    # header_row_dv = next(reader_dv)
    # for index, column_header in enumerate(header_row_dv):
    #     print(index, column_header)
    
    
    dates, highs_dv, lows_dv = [], [], []
    for row in reader_dv:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
        except:pass
        try:
            dates.append(date)
            highs_dv.append(int(row[5]))
            lows_dv.append(int(row[6]))
        except ValueError:
            print(f"Missing data for {date}")
            try:
                dates.remove(date)
            except:pass

#Sitka data part
sitka_data = 'data/sitka_weather_2018_simple.csv'
with open(sitka_data) as f:
    reader_ak = csv.reader(f) # ak for Alaska

    highs_ak, lows_ak = [], []
    for row in reader_ak:
        try:
            date = datetime.strptime(row[2], '%Y-%m-%d')
        except:pass
        try:
            highs_ak.append(int(row[5]))
            lows_ak.append(int(row[6]))
        except ValueError:
            try:
                date = datetime.strptime(row[2], '%Y-%m-%d')
                print(f"Missing data for {date}")
            except:pass
        
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 6), dpi=80)
#Plot Death Valley highs
ax.plot(dates, highs_dv, c='red', alpha=1)
#Plot Sitka highs
ax.plot(dates, highs_ak, c='blue', alpha=1)
#Compare AK and CA highs
ax.fill_between(dates, highs_ak, highs_dv, facecolor='red', alpha=0.1)

#Gives format to the plot
plt.title('Daily highs difference between Death Valley, CA & Sitka, AK | 2018', fontsize=18)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F°)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()