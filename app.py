from agenda import Agenda
from contacto import Contacto
from flask import Flask, render_template, request
from agenda import Agenda
from contacto import Contacto
from jinja2 import Template
import json

app = Flask(__name__)

#index inicio
@app.route('/')
def index():
    #return render_template('index.html')
    agenda = Agenda('agenda')
    contactos = agenda.obtenerContactos()
    return render_template('index.html', contactos=contactos)

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
    agenda = Agenda('agenda')
    contactos = agenda.obtenerContactos()
    return render_template('mostrar_agenda.html', contactos=contactos)
    
if __name__ == "__main__":
    app.run()
