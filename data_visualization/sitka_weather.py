import csv
import matplotlib.pyplot as plt

filename = './sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
    print(highs)
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
