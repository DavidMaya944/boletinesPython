from B1_P01.Persona import Persona


class Vendedor(Persona):
    def __init__(self, NIF, nombre, apellidos, usuario, password):
        super().__init__(NIF, nombre, apellidos)
        self.__usuario = usuario
        self.__password = password

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        sResultado = ""
        sResultado += "VENDEDOR: \n"
        sResultado += "-"*80
        sResultado += "\nNIF: " + super().NIF + "\n"
        sResultado += "nombre: + " + super().nombre + "\n"
        sResultado += "apellidos: " + super().apellidos + "\n"
        sResultado += "usuario: " + str(self.usuario) + "\n"
        sResultado += "password: " + self.password + "\n"

        return sResultado
