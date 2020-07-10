from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')
db = cliente['agenda']
#db = cliente.ejemplo
coleccion = db.contactos

# Operaciones Mongo
def obtenerTodo():
    cursor = coleccion.find()
    return list(cursor)

def obtenerUno(titulo):
    # resultado = coleccion.find_one({'nombre': titulo})
    resultado = coleccion.find({'nombre': {'$regex':'.*'+titulo+'.*', "$options" :'i'}})
    return list(resultado)

def insertarUno(datos):
    id = coleccion.insert_one(datos)
    return id

def editarUno(titulo, datos):
    resultado = coleccion.update_one({'nombre': titulo}, 
        {'$set': {'correo': datos['correo']}})
    return str(resultado.modified_count)