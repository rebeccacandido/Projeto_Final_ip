from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def ola():
    #return "<h1>Olá, mundo!</h1>"
    return render_template("index.html")

@app.route("/sobre-equipe")
def sobre_equipe():
    return render_template("sobre.html")

@app.route("/gemini.html")
def gemini():
    return render_template("gemini.html")

@app.route("/glossario.html")
def glossario():
    return render_template("glossario.html")


app.run()