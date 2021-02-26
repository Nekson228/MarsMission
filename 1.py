from flask import Flask, render_template
import json

app = Flask(__name__)


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
    dick = {
        'title': 'Прикол',
        'surname': 'Поглао',
        'name': 'Некит',
        'education': 'Низшее',
        'profession': 'Нету',
        'sex': 'male',
        'motivation': 'Хочу чтоб космическую станцию захватили пришельцы!',
        'ready': False,
    }
    return render_template('answer.html', **dick)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080, debug=True)
