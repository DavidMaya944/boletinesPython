from B1_P05.Persona import Persona

class Agenda:

    __agenda = []

    def __init__(self, agenda):
        self.agenda = agenda

    def guardarEnTXT(self, oPersona):
        archivo = open('agenda.txt', 'a')
        archivo.write("\nCONTACTO: " + str(oPersona))
        archivo.close()
        print("Contacto anadido")

    def leertxt(self):
        archivo = "agenda.txt"
        with open(archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)


    def buscar(self, nombre, apellido):
        f = open("agenda.txt", "r")
        lineas = f.readlines()
        if Persona.nombre.__eq__(nombre) and Persona.apellido.__eq__(apellido):
            telefono = str(Persona.telefono)
            print(telefono)
        f.close()

    def borrar(self, nombre, apellido):
        file_input = "agenda.txt"
        file_output = "agenda.txt"
        f = open(file_input, "r")
        lineas = f.readlines()
        if Persona.nombre.__eq__(nombre) and Persona.apellido.__eq__(apellido):
            f = open(file_output, "w")
            "agenda.txt".write(" ")
            print("Registro borrado")
        f.close()
