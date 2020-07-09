from agenda import Agenda
from contacto import Contacto
from flask import Flask, render_template, request
from jinja2 import Template
import json
from consultas import obtenerTodo, obtenerUno, insertarUno

app = Flask(__name__)

#index inicio
@app.route('/')
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
 
@app.route('/mostrar')
def mostrar_agenda():
    #agenda = Agenda('agenda')
    #contactos = agenda.obtenerContactos()
    contactos = obtenerTodo()
    return render_template('mostrar.html', contactos=contactos)
    
if __name__ == "__main__":
    app.run()
