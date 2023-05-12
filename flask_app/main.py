from flask import Flask, render_template, url_for
from practice import app

context = {'title': 'Заголовок',
           'text': 'Текст'}

@app.route('/')
def index():
    return render_template('index.html', context=context)


@app.route('/news')
def news():
    return "Новости"


@app.route('/news_detail/<int:id>')
def news_detail(id: int):
    return f"Новость {id}"

def run_tests():
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('news'))
        print(url_for('news_detail', id=10))

if __name__ == '__main__':
    app.run(debug=True)
