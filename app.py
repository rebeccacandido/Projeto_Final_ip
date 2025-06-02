import csv
from flask import Flask, render_template, request, url_for, redirect
from urllib.parse import unquote
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def ola():
    # return '<h1>Olá, Mundo!</h1>'
    return render_template('index.html') #aaaaa

@app.route('/sobre-equipe')
def sobre_equipe():
    return render_template('sobre.html')

genai.configure(api_key="GEMINI_API_KEY")

@app.route('/gemini', methods=["GET", "POST"])
def gemini():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        try:
            modelo = genai.GenerativeModel(model_name="gemini-2.0-flash")
            resposta_gemini = modelo.generate_content(pergunta)
            resposta = resposta_gemini.text
        except Exception as e:
            resposta = f"Erro ao acessar a IA: {e}"
    return render_template("gemini.html", resposta=resposta)


@app.route("/fundamentos")
def fundamentos():
    return render_template("fundamentos.html")


@app.route('/glossario')
def glossario():
    glossario_de_termos = []

    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for t in reader:
                if len(t) == 2:
                    glossario_de_termos.append(t)

    return render_template('glossario.html', glossario=glossario_de_termos)




@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')


@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form['termo'].strip()
    definicao = request.form['definicao'].strip()

    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for linha in reader:
                if linha and linha[0].lower() == termo.lower():
                    return redirect(url_for('glossario'))

    if termo and definicao:
        with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

@app.route('/apagar_termo/<termo>', methods=['POST'])
def apagar_termo(termo):
    termos_atualizados = []
    termo = termo.strip().lower()

    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for linha in reader:
                if linha and linha[0].strip().lower() != termo:
                    termos_atualizados.append(linha)

        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(termos_atualizados)

    return redirect(url_for('glossario'))

@app.route('/editar_termo/<termo_antigo>', methods=['POST'])
def editar_termo(termo_antigo):
    novo_termo = request.form['novo_termo'].strip()
    nova_definicao = request.form['nova_definicao'].strip()
    termo_antigo = termo_antigo.strip().lower()

    termos_atualizados = []

    if os.path.exists('bd_glossario.csv'):
        with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for linha in reader:
                if linha and linha[0].strip().lower() == termo_antigo:
                    termos_atualizados.append([novo_termo, nova_definicao])
                else:
                    termos_atualizados.append(linha)

        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(termos_atualizados)

    return redirect(url_for('glossario'))

if __name__ == '__main__':
    app.run(debug=True)
