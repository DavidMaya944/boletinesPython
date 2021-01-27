class Persona:

    def __init__(self, nombre, apellido, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__agenda = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        sResultado = ""
        sResultado += "Nombre: " + self.nombre
        sResultado += "Apellido: " + self.apellido
        sResultado += "telefono: " + self.telefono
        return sResultado