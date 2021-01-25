from ventas.presupuestos import Cliente, ModeloDePresupuesto

nombreCliente = input("Nombre: " )
apellidoCliente = input("Apellido: " )

c = Cliente(nombreCliente, apellidoCliente)

m = ModeloDePresupuesto("MEDAC", "David Maya", 30, "24/11/2019", "presupuesto", 10, 5)

m.montar_presupuesto()