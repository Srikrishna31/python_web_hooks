from flask import Flask

app = Flask(__name__, template_folder='templates')

app.secret_key = app.config['SECRET_KEY']
app.config.from_object('config')