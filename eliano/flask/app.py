from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route('/')
def index():
    return "<p>Hello Mundo</p>"
@app.route('/<name>')
def hello(name):
    return f"Bem vindo {escape(name)}!"
@app.route('/projects')
def projects():
    return "Pagina do projeto"
@app.route('/about')
def about():
    return "Página sobre"
@app.route('/login')
def login():
    return "Pagina de Login"