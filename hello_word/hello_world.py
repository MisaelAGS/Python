from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        texto = request.form.get("texto")
        return f"<p>{texto}</p>"
    return '''
        <form method="POST">
            Digite o texto a ser exibido na tela: <input type="text" name="texto">
            <input type="submit" value="Enviar">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
