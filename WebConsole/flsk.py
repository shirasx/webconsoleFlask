from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)


diretorio_atual = os.getcwd()

@app.route("/")
def index():
    return render_template("index.html", diretorio_atual=diretorio_atual)

@app.route("/executar_comando", methods=["POST"])
def executar_comando():
    global diretorio_atual
    comando = request.form.get("comando")

    if comando.startswith("cd "):
        novo_diretorio = comando[3:].strip()  
        try:
            os.chdir(novo_diretorio)
            diretorio_atual = os.getcwd()
            resultado = f"Diretório alterado para {diretorio_atual}"
        except Exception as e:
            resultado = f"Erro ao acessar o diretório: {str(e)}"
    else:
        try:
            resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            resultado = str(e.output)
        except Exception as e:
            resultado = str(e)

    return render_template("index.html", resultado=resultado, diretorio_atual=diretorio_atual)

if __name__ == "__main__":
    app.run(port=8080)
