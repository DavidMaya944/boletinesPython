from B1_P03.ventas.Presupuestos import ModeloDePresupuesto


class ModeloDePresupuestoMultiple(ModeloDePresupuesto):
    servicios = []

    def __init__(self, empresa, cliente, importe, fecha, servicio):
        super().__init__(empresa, cliente, importe, fecha, servicio)
        self.__servicios = servicio


    def addServicio(self, servicio):
        bExito = False
        if type(servicio) == ModeloDePresupuesto.servicio:
            self.servicios.append(servicio)
            bExito = True

        return bExito

    def deleteServicio(self, servicio):
        bExito = False
        if type(servicio) == ModeloDePresupuesto.servicio:
            self.servicios.remove(servicio)
            bExito = True

        return bExito

    def updateServicio(self, servicio):
        bExito = False
        if type(servicio) == ModeloDePresupuesto.servicio:
            self.servicios.update(servicio)
            bExito = True

        return bExito

    def listarServicio(self):
        sResultado = ""
        for x in self.servicios:
            sResultado += str(x)

        return sResultado