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


    def addPersona(self, oPersona):
        exito = False
        if type(oPersona) == Persona:
            self.__agenda.append(oPersona)
            exito = True

        return exito

    def deletePersona(self, oPersona):
        if type(oPersona) == Persona:
            self.__agenda.remove(oPersona)


    def updatePersona(self, oPersona):
         if type(oPersona) == Persona:
            self.__agenda.update(oPersona)


    def listarPersona(self):
        sResultado = ""
        for x in self.agenda:
            if type(x) == Persona:
                sResultado += str(x)

        return sResultado
