from operator import itemgetter

import requests
from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # безопасно берём значения.
    title = response_dict.get('title', "No title")
    comments = response_dict.get('descendants', 0)

    # Построение словаря для каждой статьи.
    submission_dict = {
        'title': title,
        'hh_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': comments,
    }
    submission_dicts.append(submission_dict)


submissions_dict = sorted(submission_dicts, key=itemgetter('comments'),
                                reverse=True)

links, comments, labels = [], [], []
for submission_dict in submissions_dict:
    article_name = submission_dict['title']
    article_url = submission_dict['hh_link']
    article_link = f"<a href='{article_url}'>{article_name}</a>"
    links.append(article_link)

    comments.append(submission_dict['comments'])

    labels.append(submission_dict['title'])


# Визуализация полученных данных
data = [{
    "type": 'bar',
    'x': links,
    'y': comments,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    "title": "Most Active Articles on Hacker News",
    'font': {'size': 28},
    'xaxis': {
        'title': {
            'text': 'Articles',
            'font': {'size': 24},
        },
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': {
            'text': 'Comments',
            'font': {'size': 24},
        },
        'tickfont': {'size': 14},
    },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename='visualization/hh_submissions_visual.html')

