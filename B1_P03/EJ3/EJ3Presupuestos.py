from B1_EJ03.ventas.Presupuestos import ModeloDePresupuesto
from B1_EJ03.ventas.Presupuestos import Cliente

nombreCliente = input("Nombre: " )
apellidoCliente = input("Apellido: " )

c = Cliente(nombreCliente, apellidoCliente)

m = ModeloDePresupuesto("MEDAC", "David Maya", 30, "24/11/2019", "presupuesto")

m.montar_presupuesto()