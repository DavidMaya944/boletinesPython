from B1_P02.Persona import Persona
from B1_P02.Pedido import Pedido
from B1_P02.Cliente import Cliente
from B1_P02.Vendedor import Vendedor
import sqlite3

class Tienda:


    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()

    def createTableCliente(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cliente(dni text PRIMARY KEY, nombre text, apellidos text, telefono integer, direccion text)")
        self.conn.commit()

    def createTableVendedor(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS vendedor(dni text PRIMARY KEY, nombre text, apellidos text, usuario text, password text)")
        self.conn.commit()

    def crearTablaPedido(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pedido(id_pedido integer AUTO_INCREMENT PRIMARY KEY, dni_cliente text, dni_vendedor text, fecha text, total real)")
        self.conn.commit()

    def altaCliente(self, cliente):
        bExito = False
        if type(cliente) == Cliente:
            self.cursor.execute("INSERT INTO cliente (dni, nombre, apellidos, telefono, direccion) VALUES('" + cliente.NIF + "', '" + cliente.nombre + "', '" + cliente.apellidos + "', '" + str(cliente.telefono) + "', '" + cliente.direccion + "')")
            self.conn.commit()
            bExito = True

        return bExito

    def altaVendedor(self, vendedor):
        bExito = False
        if type(vendedor) == Vendedor:
            self.cursor.execute("INSERT INTO vendedor (dni, nombre, apellidos, usuario, password) VALUES(" + vendedor.NIF + ", " + vendedor.nombre + ", "
                                + vendedor.apellidos + ", " + vendedor.usuario + ", " + vendedor.password)
            self.conn.commit()
            bExito = True

        return bExito

    def altaPedido(self, pedido):
        bExito = False
        if type(pedido) == Pedido:
            self.cursor.execute("INSERT INTO pedido (dni_cliente, dni_vendedor, fechaPedido, total) VALUES(" + pedido.oCliente + ", " + pedido.oVendedor + ", "
                                + pedido.fechaPedido + ", " + pedido.total)
            self.conn.commit()
            bExito = True

        return bExito

    def numClientes(self):
        suma = self.cursor.execute('SELECT COUNT(*) FROM cliente')
        return suma

    def numVendedores(self):
        suma = self.cursor.execute('SELECT COUNT(*) FROM vendedor')
        return suma

    def numPedidos(self):
        suma = self.cursor.execute('SELECT COUNT(*) FROM pedido')
        return suma

    def importeTotalPedidos(self):
        total = float(0)
        self.cursor.execute('SELECT SUM(total) FROM pedido')
        for total in self.cursor:
            print(total)
        return total

    def listadoClientes(self):
        self.cursor.execute('SELECT * FROM cliente')
        sResultado = self.cursor.fetchall()
        return sResultado

    def listadoVendedores(self):
        self.cursor.execute('SELECT * FROM vendedor')
        sResultado = self.cursor.fetchall()
        return sResultado

    def listadoPedidosFecha(self, fechaPedido):
        self.cursor.execute('SELECT * FROM pedido WHERE fecha = ' + fechaPedido)
        sResultado = self.cursor.fetchall()
        return sResultado