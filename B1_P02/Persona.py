class Persona:
    def __init__(self, NIF, nombre, apellidos):
        self.__NIF = NIF
        self.__nombre = nombre
        self.__apellidos = apellidos

    @property
    def NIF(self):
        return self.__NIF

    @NIF.setter
    def NIF(self, NIF):
        self.__NIF = NIF

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    def __str__(self):
        sResultado = ""
        sResultado += "NIF: " + self.NIF + "\n"
        sResultado += "nombre: " + self.nombre + "\n"
        sResultado += "apellidos: " + self.apellidos + "\n"

        return sResultado

