from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #INDICAR A QUE DOMINIO MANDAMOS NUESTRA API

@app.route('/')
def hello_world():
    return 'hola, mundito!'

@app.route('/api/users')
def get_users():
    return{
        'users': ['Karolay', 'Eritos', 'James']
    }

@app.route('/api/fruits')
def get_users():
    return{
        'users': ['Fresa', 'Naranja', 'Manzana']
    }

if __name__ == '__main__':
    app.run(debug=True) #by default Flask runs on port 5000
