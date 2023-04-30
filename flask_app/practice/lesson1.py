from config import app

import random
import requests

def get_finonacci(n):
    numbers = [1, 1]
    for i in range(2, n):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers

@app.route('/fibonacci')
def fibonacci():
    return ' '.join(map(str, get_finonacci(100)))


def get_course() -> str:
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = ''
    for code, data in response['Valute'].items():
        result += f'{data["Nominal"]} {data["Name"]} стоит {data["Value"]} руб.<br>'
    return result


@app.route('/money/')
def money():
    return get_course()


def get_data():
    data = []
    with open('data.txt', encoding='utf-8') as f:
        for line in f:
            data.append(line.strip())
    return data


@app.route('/random')
def citate():
    data = get_data()
    return random.choice(data)