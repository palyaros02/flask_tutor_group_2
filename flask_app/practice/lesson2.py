import datetime

from .lesson1 import app


@app.route('/<int:a>/<op>/<int:b>')
def calc(a:int, op: str, b: int):
    if op in ('+', '-', '*', ':'):
        op = '/' if op == ':' else op
        try:
            return f'{a} {op} {b} = {eval(f"{a} {op} {b}")}'
        except ZeroDivisionError:
            return f'Деление на ноль!'
    else:
        return f'Ошибка в операторе'

def get_date_or_time(mode):
    dt = datetime.datetime.now()
    if mode == 'date':
        return f'{dt.strftime("%d.%m.%Y")}'
    elif mode == 'time':
        return f'{dt.strftime("%H:%M:%S")}'
    else:
        return f'404'

app.add_url_rule("/<string:mode>", "datetime", get_date_or_time)


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