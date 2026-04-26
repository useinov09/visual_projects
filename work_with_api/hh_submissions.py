from operator import itemgetter

import requests

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


for submission_dict in submissions_dict:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hh_link']}")
    print(f"\nComments: {submission_dict['comments']}")
