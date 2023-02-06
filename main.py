from flask import Flask, redirect, url_for, request, render_template
from requests import get
import json, requests

app = Flask(__name__)

@app.route('/') #criando rota
def inicio():
  return render_template('welcome.html')
  
@app.route('/login/')
def login():
  return render_template('login.html')

@app.route('/404/')
def pne():
  return render_template('404.html')

@app.route('/check/', methods=['POST', 'GET'])
def validar():
  acesso_u = "simone"
  acesso_s = "123"
  if request.method == 'POST':
    usuario = request.form['c_usuario'] #chamando o meu usuario
    senha = request.form['c_senha']
    if usuario == acesso_u and senha == acesso_s:
      return redirect(url_for('membros'))
    else:
      return redirect(url_for('404'))
  else:
    usuario = request.args.get('c_usuario')
    senha = request.args.get('c_senha')
    if usuario == acesso_u and senha == acesso_s:
     return redirect(url_for('membros'))
    else:
      return redirect(url_for('404'))
    
@app.route('/membros/')
def membros():
  texto = "Login efetuado com sucesso"
  return texto

    
if __name__ == '__main__':
  app.run('0.0.0.0')

  #toda pagina html fica na pasta templates
