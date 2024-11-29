

import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

# Requerir el módulo de Flask
from flask import Flask, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

# Datos
albums = [
    {
        "id": 1,
        "title": "Álbum Ejemplo 1",
        "released": 2020,
        "price": 15,
        "genre": "Rock"
    },
    {
        "id": 2,
        "title": "Álbum Ejemplo 2",
        "released": 2021,
        "price": 15,
        "genre": "Rock"
    }
]

# Ruta para la página principal
@app.route('/')
def hello_world():
    return '¡Hola Mundo!'

# Ruta para obtener todos los álbumes
@app.route('/api/albums', methods=['GET'])
def get_albums():
    return jsonify(albums)

# Iniciar el servidor
if __name__ == '__main__':
    app.run(port=3000)
