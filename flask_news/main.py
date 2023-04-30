from flask import Flask


app = Flask(__name__)

index_temlate = """\
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Главная страница</h1>
        <hr>
        <p>Привет, <b>Flask</b>!</p>
        <p><a href="/news">Новости</a></p>
        <p><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"></p>
    </body>
</html>
"""


@app.route('/')
def index() -> str:
    return index_temlate

@app.route('/news')
def news():
    return "Новости"

@app.route('/news_detail/<int:id>')
def news_detail(id: int):
    return f"Новость {id}"

@app.route('/category/<string:name>')
def category(name: str):
    return f"Категория {name}"

if __name__ == '__main__':
    app.run(debug=True)