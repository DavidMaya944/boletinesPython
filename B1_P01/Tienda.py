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

    def altaCliente(self, cliente):
        bExito = False
        if type(cliente) == Cliente:
            self.__personas.append(cliente)
            bExito = True

        return bExito

    def altaVendedor(self, vendedor):
        bExito = False
        if type(vendedor) == Vendedor:
            self.__personas.append(vendedor)
            bExito = True

        return bExito

    def altaPedido(self, pedido):
        bExito = False
        if type(pedido) == Pedido:
            self.__pedidos.append(pedido)
            bExito = True

        return bExito

    def numClientes(self):
        suma = 0
        for x in self.personas:
            if isinstance(x, Cliente):
                suma += 1

        return suma

    def numVendedores(self):
        suma = 0
        for x in self.personas:
            if isinstance(x, Vendedor):
                suma += 1

        return suma

    def numPedidos(self):
        suma = 0
        for x in self.pedidos:
            if isinstance(x, Pedido):
                suma += 1

        return suma

    def importeTotalPedidos(self):
        total = float(0)
        for x in self.pedidos:
                total += float(x.total)

        return total

    def listadoClientes(self):
        sResultado = ""
        for x in self.personas:
            if type(x) == Cliente:
                sResultado += str(x)

        return sResultado

    def listadoVendedores(self):
        sResultado = ""
        for x in self.personas:
            if type(x) == Vendedor:
                sResultado += str(x)

        return sResultado

    def listadoPedidosFecha(self, fechaPedido):
        sResultado = ""
        for x in self.pedidos:
            if type(x) == Pedido:
                sResultado += str(x)

        return sResultado