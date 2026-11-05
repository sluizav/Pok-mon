from flask import Flask, render_template
import requests

app = Flask(__name__)

# rotas serso inseridas aqui
@app.route('/')
def inicio():
    id_sorteado = random.randint(1,102)
    url_api = 'https://pokeapi.co/api/v2/pokemon-form/25'(+id_sorteado)
    response = requests.get(url_api)
    dados = response.json()
    print(dados.get("name"))
    return render_template('index.html',nome=dados.get("name"))



if __name__ == '__main__':
     app.run(debug=True)

    