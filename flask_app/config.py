from flask import Flask, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '1238765ruhvsdjhft8hy2t345qjkhgfbi87yasdftbof8aw37495tb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False