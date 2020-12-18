from flask import Flask
from products.view import name

app = Flask(__name__)

@app.route('/<name>')

def index(name):
    if len(name) <5 :
        return "Hola {}".format(name)
    return "Hola {}".format(name)

app.register_blueprint(name)

if __name__ == "__main__":
    app.run(debug=True)
