from B1_P01.Cliente import Cliente
from B1_P01.Pedido import Pedido
from B1_P01.Vendedor import Vendedor

c = Cliente("53284386X", "David", "Maya", 646000204, "Calle falsa, 123")

v = Vendedor("42132455Y", "Rodrigo", "Fernandez", "roFe12", "user1234")

p = Pedido(c, v, "12/02/2019", 5000)

print("El cliente " + str(c) + "le hace un pedido " + str(p) + " al vendedor " + str(v))