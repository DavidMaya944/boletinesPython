class Persona:
    def __init__(self, NIF, nombre, apellidos):
        self.NIF(NIF)
        self.nombre(nombre)
        self.apellidos(apellidos)

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
        sResultado += "NIF: " + self.NIF()
        sResultado += "nombre: " + self.nombre()
        sResultado += "apellidos: " + self.apellidos() 

