import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')
ax.set_title('2018年7月每日最高温度', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("温度", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.rcParams['font.sans-serif'] = ['Kaitt', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
