import csv
from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib.pyplot import title

with open('data/death_valley_2018_simple.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получение дат, температурных минимумов и максимумов из файла.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Нанесение данных на диаграмму
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграммы.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()