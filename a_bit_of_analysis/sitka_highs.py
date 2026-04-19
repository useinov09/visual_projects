import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получение дат, температурных максимумов из файла.
    dates, highs = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(date)
        highs.append(high)

# Нанесение данных на диаграмму
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Форматирование диаграммы.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()