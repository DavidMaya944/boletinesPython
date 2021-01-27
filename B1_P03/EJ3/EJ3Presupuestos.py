from B1_P03.ventas.Presupuestos import ModeloDePresupuesto
from B1_P03.ventas.Presupuestos import Cliente
from B1_P03.ventas.PresupuestosMultiples import ModeloDePresupuestoMultiple
nombreCliente = input("Nombre: " )
apellidoCliente = input("Apellido: " )

c = Cliente(nombreCliente, apellidoCliente)
servicios = [("Cobrar", 20), ("Consultar", 30), ("Mantenimiento", 40), ("Presupuesto", 60)]
#m = ModeloDePresupuesto("MEDAC", c, 30, "24/11/2019", "presupuesto")

#m.montar_presupuesto()

mPm = ModeloDePresupuestoMultiple("MEDAC", c, 30, "24/11/2019", servicios)

mPm.addServicio("cobrar")

mPm.searchServicio()