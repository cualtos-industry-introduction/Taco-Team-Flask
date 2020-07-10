from agenda import Agenda
from contacto import Contacto
from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Template
import json
from consultas import obtenerTodo, obtenerUno, insertarUno

app = Flask(__name__)

#index inicio
@app.route('/')
def index():
    return render_template('index.html')

#agregar
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        datos = {}
        datos['nombre'] = request.form['nombre']
        datos['empresa'] = request.form['empresa']
        datos['correo'] = request.form['correo']
        datos['telefono'] = request.form['telefono']
        datos['nota'] = request.form['nota']
        insertarUno(datos)
        return redirect(url_for('mostrar_agenda'))
    elif request.method == 'GET':
        return render_template('agregar.html')

#buscar
@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        return redirect(url_for('buscar_resultado', nombre=request.form['nombre']))
    elif request.method == 'GET':
        return render_template('buscar.html')

@app.route('/buscar/<nombre>')
def buscar_resultado(nombre):
    resultado = obtenerUno(nombre)
    return render_template('buscarres.html', resultado=resultado)
 
@app.route('/mostrar')
def mostrar_agenda():
    #agenda = Agenda('agenda')
    #contactos = agenda.obtenerContactos()
    contactos = obtenerTodo()
    return render_template('mostrar.html', contactos=contactos)
    
if __name__ == "__main__":
    app.run()
