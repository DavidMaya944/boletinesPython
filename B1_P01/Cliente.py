from B1_P01.Persona import Persona

class Cliente(Persona):

    def __init__(self, NIF, nombre, apellidos, telefono, direccion):
        super.__init__(self, NIF, nombre, apellidos)
        self.telefono(telefono)
        self.direccion(direccion)

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = int (telefono)

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    def __str__(self):        
        sResultado = ""
        sResultado += "CLIENTE: " + super.__str__
        sResultado += "telefono: " + self.telefono()
        sResultado += "direccion: " + self.direccion() 
