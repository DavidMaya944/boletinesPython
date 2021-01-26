from B1_P02.Cliente import Cliente
from B1_P02.Pedido import Pedido
from B1_P02.Vendedor import Vendedor
from B1_P02.Tienda import Tienda


c = Cliente("53284386X", "David", "Maya", 646000204, "Calle falsa, 123")
c1 = Cliente("45521789G", "Pepe", "Martin", 645128793, "Calle falsa, 124")
c2 = Cliente("53478213S", "Manolo", "Gutierrez", 654872944, "Calle falsa, 125")

v = Vendedor("1245789W", "Romano", "Aspas", 645200314, "Calle de al lao, 456")

p = Pedido(c, v, "12/02/2019", 5000)
p1 = Pedido(c, v, "20/03/2015", 300)
p2 = Pedido(c, v, "05/02/2017", 7000)

t = Tienda()

if t.createTableCliente():
    print("La tabla CLIENTE se ha creado con exito")
else:
    print("ERROR: No se ha podido crear la tabla CLIENTE")

if t.createTableVendedor():
    print("La tabla VENDEDOR se ha creado con exito")
else:
    print("ERROR: No se ha podido crear la tabla VENDEDOR")

if t.crearTablaPedido():
    print("La tabla PEDIDO se ha creado con exito")
else:
    print("ERROR: No se ha podido crear la tabla PEDIDO")

if t.altaCliente(c):
    print("Se ha insertado el PRIMER CLIENTE con exito")
else:
    print("ERROR: PRIMER CLIENTE fallido")

if t.altaCliente(c1):
    print("Se ha insertado el SEGUNDO CLIENTE con exito")
else:
    print("ERROR: SEGUNDO CLIENTE fallido")

if t.altaCliente(c2):
    print("Se ha insertado el TERCER CLIENTE con exito")
else:
    print("ERROR: TERCER CLIENTE fallido")

if t.altaVendedor(v):
    print("Se ha insertado el VENDEDOR con exito")
else:
    print("ERROR: VENDEDOR fallido")

if t.altaPedido(p):
    print("Se ha insertado el PRIMER PEDIDO con exito")
else:
    print("ERROR: EL PRIMER PEDIDO fallido")

if t.altaPedido(p1):
    print("Se ha insertado el PRIMER PEDIDO con exito")
else:
    print("ERROR: EL PRIMER PEDIDO fallido")

if t.altaPedido(p2):
    print("Se ha insertado el PRIMER PEDIDO con exito")
else:
    print("ERROR: EL PRIMER PEDIDO fallido")

print(t.listadoClientes())

print("-"*80)

print(t.listadoVendedores())

print("-"*80)

print(t.listadoPedidosFecha("12/02/2019"))

print("El numero de clientes es: " + str(t.numClientes()))
print("El numero de vendedores es: " + str(t.numVendedores()))
print("El numero de pedidos es: " + str(t.numPedidos()))

print("Importe total: " + str(t.importeTotalPedidos()))