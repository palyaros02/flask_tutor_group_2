from flask import Flask, url_for

import random

import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Главная страница"


@app.route('/news')
def news():
    return "Новости"


@app.route('/news_detail/<int:id>')
def news_detail(id: int):
    return f"Новость {id}"


def get_finonacci(n):
    numbers = [1, 1]
    for i in range(2, n):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers


@app.route('/fibonacci')
def fibonacci():
    return ' '.join(map(str, get_finonacci(n)))


def get_course() -> str:
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    result = ''
    for code, data in response['Valute'].items():
        result += f'{data["Nominal"]} {data["Name"]} стоит {data["Value"]} руб.<br>'
    return result


@app.route('/money')
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


@app.route('/total/<int:a>/<int:b>')
def total(a, b):
    return f'a + b = {a + b}'


def get_primes(n):
    primes = []
    current = 2
    while len(primes) < n:
        for i in range(2, current):
            if current % i == 0:
                break

        else:
            primes.append(current)

        current += 1
    return " ".join(map(str, primes))


app.add_url_rule("/primes/<int:n>", "primes", get_primes)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('news'))
    print(url_for('news_detail', id=10))

if __name__ == '__main__':
    n = 100
    app.run(debug=True)
