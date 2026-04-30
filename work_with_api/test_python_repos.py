import requests

import unittest

def get_api():
    """Создание вызова API и сохранение ответа."""
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    return r

class TestPythonRepos(unittest.TestCase):
    def setUp(self):
        """Складываем нужные значения в переменные"""
        self.r = get_api()
        self.response_dict = self.r.json()

    def test_api(self):
        """Проверяем ответ api"""
        self.assertEqual(self.r.status_code, 200 )

    def test_total_count_repositories(self):
        """Проверка общего количества репозиториев"""
        self.assertGreater(self.response_dict['total_count'], 2000)


    def test_count_repositories(self):
        """Проверка количества вывода репозиториев"""
        self.assertEqual(len(self.response_dict['items']), 30)

if __name__ == '__main__':
    unittest.main()