from B1_P01.Persona import Persona
from B1_P01.Pedido import Pedido

class Tienda:
    def __init__(self, personas, pedido):
        self.personas(personas)
        self.pedido(pedido)

    @property
    def personas(self):
        return self.__personas
    
    @personas.setter
    def personas(self, personas):
        self.__personas = Persona(personas)
    
    @property
    def pedido(self):
        return self.__pedido
    
    @pedido.setter
    def pedido(self, pedido):
        self.__pedido = Pedido(pedido)

    def altaCliente(Cliente)
        

    