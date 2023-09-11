from flask import Flask, render_template, request
import requests
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/executar_comando", methods=["POST"])
def executar_comando():
    comando = request.form.get("comando")
    
    # Executar o comando usando subprocess
    try:
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        resultado = str(e.output)
    
    # Renderize o mesmo template com o resultado
    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(port=8080)
