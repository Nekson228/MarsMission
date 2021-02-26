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
def news(item):
    with open("news.json", "rt", encoding="utf8") as f:
        prof_list = json.loads(f.read())
    return render_template('news.html', news=prof_list, item=item)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080, debug=True)
