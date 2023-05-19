from datetime import datetime
from unicodedata import category

from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = 'asdasdasdae2weqwe123'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///news.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Category(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)

    news = db.relationship('News', back_populates='category')

    def __repr__(self):
        return f'<Category({self.id=}, {self.title=})>'

class News(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    category = db.relationship('Category', back_populates='news')

    def __repr__(self):
        return f'<News({self.id=}, {self.title=}, {self.text=}, {self.created_date=}, {self.category=})>'

db.create_all()

def get_categories():
    categories = Category.query.all()
    return [(c.id, c.title) for c in categories]

class NewsForm(FlaskForm):
    title = StringField(
        'Заголовок новости',
        validators=[
            DataRequired(message='Поле не должно быть пустым'),
            Length(min=5, max=255, message='Длина строки должна быть от 5 до 255 символов')
        ]
    )
    text = TextAreaField(
        'Текст новости',
        validators=[
            DataRequired(message='Поле не должно быть пустым')
        ]
    )
    categories = SelectField('Категория',choices=get_categories())
    submit = SubmitField('Добавить новость')


@app.route('/')
def index():
    news = News.query.all()
    categories = Category.query.all()
    return render_template('index.html',
                           news=news[::-1],
                           categories=categories)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news_item = News.query.get(id)
    categories = Category.query.all()
    return render_template('news_detail.html',
                           news=news_item,
                           categories=categories)

@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    categories = Category.query.all()
    form = NewsForm()
    if form.validate_on_submit():
        news_item = News(
            title=form.title.data,
            text=form.text.data,
            category_id=form.categories.data
        )
        db.session.add(news_item)
        db.session.commit()
        return redirect(url_for('add_news'))
    return render_template('add_news.html',
                           form=form,
                           categories=categories)

@app.route('/category/<int:id>')
def news_in_category(id):
    category = Category.query.get(id)
    news = category.news
    category_name = category.title
    categories = Category.query.all()
    return render_template('category.html',
                           news=news,
                           category_name=category_name,
                           categories=categories)


if __name__ == '__main__':
    app.run(debug=True)
