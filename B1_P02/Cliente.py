from B1_P01.Persona import Persona

class Cliente(Persona):

    def __init__(self, NIF, nombre, apellidos, telefono, direccion):
        super().__init__(NIF, nombre, apellidos)
        self.__telefono = telefono
        self.__direccion = direccion

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = int(telefono)

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    def __str__(self):        
        sResultado = ""
        sResultado += "CLIENTE: \n"
        sResultado += "-"*80
        sResultado += "\nNIF: " + super().NIF + "\n"
        sResultado += "nombre: " + super().nombre + "\n"
        sResultado += "apellidos: " + super().apellidos + "\n"
        sResultado += "telefono: " + str(self.telefono) + "\n"
        sResultado += "direccion: " + self.direccion + "\n"

        return sResultado
