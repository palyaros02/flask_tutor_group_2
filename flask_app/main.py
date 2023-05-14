from cgitb import text

from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from practice import app
from wtforms import (EmailField, SelectField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import DataRequired, Email, Optional

db = SQLAlchemy(app)

class Feedback(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(64))
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Feedback({self.id=}, {self.name=}, {self.text=}, {self.email=}, {self.rating=})>'

db.create_all()

context = {'title': 'Заголовок',
           'text': 'Текст'}

class FeedbackForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(message='Имя не может быть пустым')])
    text = TextAreaField('Отзыв', validators=[DataRequired(message='Отзыв не может быть пустым')])
    email = EmailField('Ваш Email', validators=[Optional(), Email('Некорректный email')])
    rating = SelectField('Ваша оценка?', choices=[1,2,3,4,5])
    submit = SubmitField('Добавить')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()
    feedbacks = Feedback.query.all()
    if form.validate_on_submit():
        feedback = Feedback(
            name=form.name.data,
            text=form.text.data,
            email=form.email.data,
            rating=form.rating.data,
        )
        db.session.add(feedback)
        db.session.commit()
        return redirect('/')
    return render_template('index.html', form=form, feedbacks=feedbacks)


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
