from B1_P05.Persona import Persona


class Agenda:

    def __init__(self, oPersona):
        self.__oPersona = oPersona
        self.__agenda = []

    def addPersona(self, oPersona):
        for x in self.__agenda:
            if type(oPersona) == Persona:
                self.__agenda.append(oPersona)


    def deletePersona(self, oPersona):
        for x in self.__agenda:
            if type(oPersona) == Persona:
                self.__agenda.remove(oPersona)


    def updatePersona(self, oPersona):
        for x in self.__agenda:
            if type(oPersona) == Persona:
                self.__agenda.update(oPersona)


    def listarPersona(self):
        sResultado = ""
        for x in self.__agenda:
            sResultado += x

        return sResultado
