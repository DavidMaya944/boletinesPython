from B1_P03.ventas.Presupuestos import ModeloDePresupuesto


class ModeloDePresupuestoMultiple(ModeloDePresupuesto):
    servicios = [("Cobrar", 20), ("Consultar", 30), ("Mantenimiento", 40), ("Presupuesto", 60)]

    def __init__(self, empresa, cliente, importe, fecha, servicio):
        super().__init__(empresa, cliente, importe, fecha, servicio)
        self.__servicios = servicio

