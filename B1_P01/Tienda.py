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
        self.__personas = personas
    
    @property
    def pedidos(self):
        return self.__pedidos
    
    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos = pedidos

    def altaCliente(self, Cliente):
        bExito = False
        if type(Cliente) == Cliente:
            self.__personas.append(Cliente)
            bExito = True

        return bExito

    def altaVendedor(self, Vendedor):
        bExito = False
        if type(Vendedor) == Vendedor:
            self.__personas.append(Vendedor)
            bExito = True

        return bExito

    def altaPedido(self, Pedido):
        bExito = False
        if type(Pedido) == Pedido:
            self.__pedidos.append(Pedido)
            bExito = True

        return bExito

    def numClientes(self):
        suma = 0
        for x in self.personas:
            if type(Persona) == Cliente:
                suma += x[0]

        return suma

    def numVendedores(self):
        suma = 0
        for x in self.personas:
            if type(Persona) == Vendedor:
                suma += x[0]

        return suma

    def numPedidos(self):
        suma = 0
        for x in self.pedidos:
            suma += x[0]

        return suma

    def importeTotalPedidos(self):
        total = 0
        for x in self.pedidos:
            total += x[0]

        return total

    def listadoClientes(self):
        sResultado = ""
        for x in self.personas:
            if type(Cliente) == Cliente:
                sResultado = x[0]

        return sResultado

    def listadoVendedores(self):
        sResultado = ""
        for x in self.personas:
            if type(Vendedor) == Vendedor:
                sResultado = x[0]

        return sResultado

    def listadoPedidosFecha(self, fechaPedido):
        sResultado = ""
        for x in self.pedidos:
            if type(Pedido.fechaPedido) == fechaPedido:
                sResultado = x[0]

        return sResultado