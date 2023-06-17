import requests
import datetime

# URL для получения списка вопросов на Stack Overflow
url = 'https://api.stackexchange.com/2.3/questions'

# Параметры запроса
params = {
    'fromdate': int((datetime.datetime.now() - datetime.timedelta(days=2)).timestamp()),
    'todate': int(datetime.datetime.now().timestamp()),
    'order': 'desc',
    'sort': 'activity',
    'tagged': 'python',
    'site': 'stackoverflow'
}

# Выполнение запроса
response = requests.get(url, params=params)

# Обработка ответа
if response.status_code == 200:
    questions = response.json()['items']
    for question in questions:
        print(question['title'])
else:
    print('Произошла ошибка при выполнении запроса.')