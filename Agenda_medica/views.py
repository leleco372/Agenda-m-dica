from main import app
from flask import render_template
from flask import request, redirect, url_for
import sqlite3

@app.route("/")
def homepage():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["usuario"]
    password = request.form["senha"]

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
    "SELECT * FROM usuarios WHERE (email = ? OR nome = ?) AND senha = ?",
    (username, username, password))

    usuario = cursor.fetchone()

    conexao.close()

    if usuario:
        return redirect(url_for("/agenda"))
    else:
        return render_template(
            "login.html",
            error="Usuário ou senha inválidos."
        )
    @app.route("/agenda")
    def agenda():
        return render_template("agenda.html")