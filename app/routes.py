from app import app
from flask import render_template
from flask import request

@app.route('/') #configurando uma rota web
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Inicial", nome="Fernanda")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Fernanda")

@app.route('/colecoes')
def colecoes():
    return render_template('colecoes.html', titulo="Coleções", nome="Fernanda")

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo="Sobre", nome="Fernanda")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro", nome="Fernanda")

@app.route('/parceiros')
def parceiros():
    return render_template('parceiros.html', titulo="Parceiros", nome="Fernanda")