from flask import Flask
from rutas import rutas  # Importa el blueprint de rutas

app = Flask(__name__)

# Registrar el blueprint de personas
app.register_blueprint(rutas)

if __name__ == '__main__':
    app.run(debug=True)
