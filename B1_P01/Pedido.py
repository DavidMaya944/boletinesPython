class Pedido:
    def __init__(self, oCliente, oVendedor, fechaPedido, total):
        self.oCliente(oCliente)
        self.oVendedor(oVendedor)
        self.fechaPedido(fechaPedido)
        self.total(total)

@property
def oCliente(self):
    return self.__oCliente

@oCliente.setter
def oCliente(self, oCliente):
    self.__oCliente = oCliente

@property
def oVendedor(self):
    return self.__oVendedor

@oVendedor.setter
def oVendedor(self, oVendedor):
    self.__oVendedor = oVendedor

@property
def fechaPedido(self):
    return self.__fechaPedido

@fechaPedido.setter
def fechaPedido(self, fechaPedido):
    self.__fechaPedido = fechaPedido

@property
def total(self):
    return self.__total

@total.setter
def total(self, total):
    self.__total = float(total)

def __str__(self):
    sResultado = ""
    sResultado += "Cliente: " + self.oCliente()
    sResultado += "Vendedor: " + self.oVendedor()
    sResultado += "Fecha: " + self.fechaPedido()
    sResultado += "Total: " + self.total()