from flask import Flask
from cliente import cliente

app = Flask (__name__)
app.register_blueprint()

@app.route('/', methods=['GET'])
def hello():
    return "Hola mundo"

if __name__ == "__main__":

    app.run(host = '0.0.0.0', debug = True, port = '5003')
    app.run(debug = True)