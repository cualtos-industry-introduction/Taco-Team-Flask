from flask import Flask, render_template, request
import json

app = Flask(__name__)

#index inicio
@app.route('/index')
def index():
    
    return render_template('index.html')

#agregar
@app.route('/agregar')
def agregar():
    
    return render_template('agregar.html')

#buscar
@app.route('/buscar')
def buscar():
    
    return render_template('buscar.html')

 

if __name__ == "__main__":
    app.run()
