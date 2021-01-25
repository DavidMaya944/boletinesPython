from B1_P01.Persona import Persona

class Vendedor(Persona):
    def __init__(self, NIF, nombre, apellidos, usuario, password):
        super.__init__(NIF, nombre, apellidos)
        self.usuario(usuario)
        self.password(password)

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
    sResultado += "VENDEDOR: " + super.__str__
    sResultado += "usuario: " + self.usuario()
    sResultado += "password: " + self.password()