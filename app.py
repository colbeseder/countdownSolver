from flask import Flask
import requests
import numbersSolver, lettersSolver, resources.dictionaryHelper

app = Flask(__name__)
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static')


@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/static/<file>')
def static_files(file):
    return app.send_static_file(file)

@app.route('/api/numbers/<cards>/<target>')
def numbers(cards, target):
    return numbersSolver.getReadableSolution(cards.split(","), target)

@app.route('/api/letters/<cards>')
def letters(cards):
    return lettersSolver.solve(cards)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    resources.dictionaryHelper.prepFromDefault()
    app.run(host='0.0.0.0')
