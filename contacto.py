class Contacto:

    def __init__(self, info):
        # se manda los string como parámetros
        if isinstance(info, str):
            self.nombre = info
            self.empresa = ""
            self.correo = ""
            self.telefono = ""
            self.nota = ""
        # se manda el diccionario de datos como constructor
        elif isinstance(info, dict):
            self.nombre = info['nombre']
            self.empresa = info['empresa']
            self.correo = info['correo']
            self.telefono = info['telefono']
            self.nota = info['nota']
        else:
            raise TypeError

    def obtenerDatos(self):
        return self.__dict__
