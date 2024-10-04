from flask import Flask
import requests
import json

app = Flask(__name__)

# Sua chave de API do Google
API_KEY = 'AIzaSyBHBi2HFQ8xhYmRSheSntYKUdvq4Pu277k'  # Substitua pela sua chave de API real

# URL da API
API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}'

@app.route('/')
def home():
    return '''
        <h1>API Gemini</h1>
        <p>Faça perguntas usando a seguinte URL:</p>
        <p><strong>/ask/seu_pergunta_aqui</strong></p>
        <p>Exemplo: <strong>/ask/qual%20é%20o%20presidente%20do%20brasil</strong></p>
    '''

@app.route('/ask/<question>')
def ask_gemini(question):
    # Cabeçalhos da requisição
    headers = {
        'Content-Type': 'application/json',
    }

    # Corpo da requisição com a pergunta extraída da URL
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": question  # Inserindo a pergunta da URL aqui
                    }
                ]
            }
        ]
    }

    # Fazendo a requisição POST à API
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    # Verificando a resposta da API
    if response.status_code == 200:
        result = response.json()

        # Extraindo apenas a resposta gerada pela API
        try:
            answer = result['contents'][0]['parts'][0]['text']
        except (KeyError, IndexError):
            return "Erro ao processar a resposta da API."

        # Exibindo apenas a resposta no navegador
        return f"<h2>Resposta:</h2><p>{answer}</p>"
    else:
        return f"Erro: {response.status_code}\n{response.text}"

if __name__ == '__main__':
    app.run(debug=True)
