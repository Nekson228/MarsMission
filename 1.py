from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import json

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof: str):
    prof = prof.lower()
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    with open("static/json/profs.json", "rt", encoding="utf8") as f:
        prof_list = json.loads(f.read())
    return render_template('list.html', profs=prof_list, list_type=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        'title': 'Прикол',
        'surname': 'Поглао',
        'name': 'Некит',
        'education': 'Низшее',
        'profession': 'Нету',
        'sex': 'male',
        'motivation': 'Хочу чтоб космическую станцию захватили пришельцы!',
        'ready': False,
    }
    return render_template('answer.html', **data)


class DoubleProtectionForm(FlaskForm):
    astronaut_id = StringField('ID Астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль Астронавта', validators=[DataRequired()])
    captain_id = StringField('ID Капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль Капитана', validators=[DataRequired()])
    submit = SubmitField('Получить доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = DoubleProtectionForm()
    if form.validate_on_submit():
        return redirect('/login/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/login/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 8080, debug=True)
