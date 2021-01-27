from B1_P02.Cliente import Cliente
from B1_P02.Pedido import Pedido
from B1_P02.Vendedor import Vendedor
from B1_P02.Tienda import Tienda


c = Cliente("53284386X", "David", "Maya", 646000204, "Calle falsa, 123")
c1 = Cliente("45521789G", "Pepe", "Martin", 645128793, "Calle falsa, 124")
c2 = Cliente("53478213S", "Manolo", "Gutierrez", 654872944, "Calle falsa, 125")
c3 = Cliente("45210345M", "Luis", "Garcia", 785124320, "Calle inventada, 159")

v = Vendedor("1245789W", "Romano", "Aspas", 645200314, "Calle de al lao, 456")

p = Pedido(c, v, "12/02/2019", 5000)
p1 = Pedido(c, v, "20/03/2015", 300)
p2 = Pedido(c, v, "05/02/2017", 7000)
p3 = Pedido(c1, v, "03/07/2010", 3710)

t = Tienda()

t.createTableCliente()

t.createTableVendedor()

t.crearTablaPedido()

t.altaCliente(c)
t.altaCliente(c1)
t.altaCliente(c2)

t.altaVendedor(v)

t.altaPedido(p)

t.altaPedido(p1)
t.altaPedido(p2)

t.altaCliente(c3)
t.altaPedido(p3)

print(t.listadoClientes())

print("-"*80)

print(t.listadoVendedores())

print("-"*80)

print(t.listadoPedidosFecha("12/02/2019"))

print("El numero de clientes es: " + str(t.numClientes()))
print("El numero de vendedores es: " + str(t.numVendedores()))
print("El numero de pedidos es: " + str(t.numPedidos()))

print("Importe total: " + str(t.importeTotalPedidos()))