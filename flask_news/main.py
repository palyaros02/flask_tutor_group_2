from flask import Flask, render_template

app = Flask(__name__)

news_list = [
        {
            "title": 'Заголовок новости 1',
            "text": 'Текст новости 1'
        },
    ]

@app.route('/')
def index():
    context = dict(
        title='Главная страница',
        text='Скоро тут будут <b>новости</b>!'
    )
    return render_template(
        'index.html',
        context=context
    )

@app.route('/news')
def news():
    return "Новости"

@app.route('/news_detail/<int:id>')
def news_detail(id: int):
    context = dict(
        title=news_list[id]['title'],
        text=news_list[id]['text'],
    )
    return render_template('news_detail.html', **context)

@app.route('/category/<string:name>')
def category(name: str):
    return f"Категория {name}"

if __name__ == '__main__':
    app.run(debug=True)