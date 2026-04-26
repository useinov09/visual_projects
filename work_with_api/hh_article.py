import requests
import json

# Вызов API и сохранение ответа.
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Анализ структуры данных.
response_json = r.json()
readable_file = 'data/readable_hh_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_json, f, indent=4)
