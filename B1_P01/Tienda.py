from B1_P01.Persona import Persona
from B1_P01.Pedido import Pedido
from B1_P01.Cliente import Cliente
from B1_P01.Vendedor import Vendedor

class Tienda:
    __personas = []
    __pedidos = []

    def __init__(self, personas, pedidos):
        self.__personas = personas
        self.__pedidos = pedidos


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

    def altaCliente(self, Cliente):
        if(type(Cliente) == Cliente):
            self.__personas.append(Cliente)
            bExito = True

        return bExito

    def altaVendedor(self, Vendedor):
        if(type(Vendedor) == Vendedor):
            self.__personas.append(Vendedor)
            bExito = True

        return bExito

    def altaPedido(self, Pedido):
        if(type(Pedido) == Pedido):
            self.__pedidos.append(Pedido)
            bExito = True

        return bExito

    def numClientes(self):
        suma = 0
        for x in self.personas:
            if(type(Cliente)):
                suma += x[0]

        return suma

    def numVendedores(self):
        suma = 0
        for x in self.personas:
            if(type(Vendedor)):
                suma += x[0]

        return suma

    def numPedidos(self):
        suma = 0
        for x in self.pedidos:
            if(type(Pedido)):
                suma += x[0]

        return suma

    