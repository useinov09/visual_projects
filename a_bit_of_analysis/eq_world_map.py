import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Загрузка файла
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Получение заголовка
title = all_eq_data['metadata']['title']

# Сохраняем данные
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Нанесение данных на карту.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
    'color': mags,
    'colorscale': 'Blackbody',
    'reversescale': True,
    'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='visualizations/global_earthquakes.html')