from flask import Flask
import requests
import json

app = Flask(__name__)


API_KEY = 'AIzaSyBHBi2HFQ8xhYmRSheSntYKUdvq4Pu277k'  # Substitua pela sua chave de API real


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
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": question  
                    }
                ]
            }
        ]
    }

    
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    
    if response.status_code == 200:
        result = response.json()

        
        try:
            answer = result['contents'][0]['parts'][0]['text']
        except (KeyError, IndexError):
            return "Erro ao processar a resposta da API."

        
        return f"<h2>Resposta:</h2><p>{answer}</p>"
    else:
        return f"Erro: {response.status_code}\n{response.text}"

if __name__ == '__main__':
    app.run(debug=True)
