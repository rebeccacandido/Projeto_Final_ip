import csv
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def ola():
    #return "<h1>Olá, mundo!</h1>"
    return render_template("index.html")

@app.route("/sobre-equipe")
def sobre_equipe():
    return render_template("sobre.html")

@app.route("/gemini")
def gemini():
    return render_template("gemini.html")

@app.route("/glossario")
def glossario():

    glossario_de_termos = []

    with open("bd_glossario.csv", newline ="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")

        for t in reader:
            glossario_de_termos.append(t)

    return render_template("glossario.html", glossario=glossario_de_termos)

@app.route("/novo_termo")
def novo_termo():
    return render_template("novo_termo.html")

@app.route("/criar_termo", methods=["POST"])
def criar_termo():

    termo = request.form["termo"]
    definicao = request.form["definicao"]

    with open("bd_glossario.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow([termo, definicao])

    return redirect(url_for("glossario"))

@app.route("/excluir_termo/<int:termo_id", methods=["POST"])
def excluir_termo(termo_id):

    with open("bd_glossario.csv", "r", newline="") as file:
        reader = csv.reader(file)
        linhas = list(reader)

        for i, linha in enumerate(linhas):
            if i == termo_id:
                del linhas[i]
                break

    with open("bd_glossario.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(linha)

    return redirect(url_for("glossario"))



app.run()