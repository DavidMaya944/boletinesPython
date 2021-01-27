
from B1_P05.Persona import Persona


class Agenda:

    __agenda = []

    def __init__(self, agenda):
        self.agenda = agenda


    def meterEnArray(self, oPersona):
        for x in self.agenda:
            if type(oPersona) == Persona:
                self.agenda.append(oPersona)

    def buscarEnAgenda(self, name, lastname):
        resultado = None
        for i in self.agenda:
            if (i.nombre == name and i.apellido == lastname):
                resultado = i
        return resultado

    def cargarFichero(self):
        f = open("agenda.txt", "r")
        linea = f.readline()
        while linea != "":
            nombre = f.readline()
            apellido = f.readline()
            telefono = f.readline()
            nombre = nombre[:-1]
            apellido = apellido[:-1]
            telefono = telefono[:-1]
            self.agenda.append(nombre, apellido, telefono)
            linea = f.readline()
        f.close()
        return self.agenda

    def imprimirArray(self):
        resultado = ""
        for i in self.agenda:
            resultado += (i.str())
        return resultado

    def meterEnFichero(self):
        f = open("agenda.txt", "w")
        for i in self.agenda:
            f.write(i.str())
        f.close