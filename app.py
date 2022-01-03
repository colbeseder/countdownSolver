from flask import Flask
import requests
import numbersSolver, lettersSolver

app = Flask(__name__)
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static')


@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/api/numbers/<cards>/<target>')
def numbers(cards, target):
    solution = numbersSolver.Solution(cards.split(","), target)
    return solution.get()

@app.route('/api/letters/<cards>')
def letters(cards):
    return lettersSolver.solve(cards)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    print("running")
    app.run(host='0.0.0.0')
