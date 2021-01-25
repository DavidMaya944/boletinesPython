print("Modelos de presupuestos") 

class ModeloDePresupuesto: 

    # Metodo constructor   
    def __init__(self, titulo, encabezado_nombre, encabezado_web, encabezado_email,
    empresa, cliente, importe, fecha, servicio, monto_iva, neto):         
        print(self.divline) 
        print("\tGENERACIÓN DEL PRESUPUESTO")
        print(self.divline)
        self.__titulo = titulo;
        self.__encabezado_nombre = encabezado_nombre;
        self.__encabezado_web = encabezado_web;
        self.__encabezado_email = encabezado_email;
        self.__empresa = empresa;
        self.__cliente = cliente;
        self.__importe = importe;
        self.__fecha = fecha;
        self.__servicio = servicio;
        self.__monto_iva = monto_iva;
        self.__neto = neto;
    # Datos comerciales     
    titulo = "PRESUPUESTO"
    encabezado_nombre = "Eugenia Bahit"
    encabezado_web = "www.eugeniabahit.com.ar"
    encabezado_email = "mail@mail.com"

    # Datosimpositivos     
    IVA = 21

    # Propiedades relativas al formato     
    divline = "="*80

    # Setear los datos del cliente 
    @property
    def empresa(self):
        return self.__empresa;

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa;

    @property
    def cliente(self):
        return self.__cliente;

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente;

        
    # Setear los datos basicos del presupuesto
    @property
    def fecha(self):
        return self.__fecha;

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha;

    @property
    def servicio(self):
        return self.__servicio;

    @servicio.setter
    def servicio(self, servicio):
        self.__servicio = servicio;

    @property
    def importe(self):
        return self.__importe;

    @importe.setter
    def importe(self, importe):
        self.__importe = importe;

    @property
    def vencimiento(self):
        return self.__vencimiento;
    
    @vencimiento.setter
    def vencimiento(self, vencimiento):
        self.__vencimiento = vencimiento;
        
    # Calcular IVA
   
    def calcular_iva(self):         
        self.__monto_iva = self.importe*self.IVA/100
        
    # Calcula el monto total del presupuesto   
    @property
    def neto(self):
        return self.__neto;

    @neto.setter
    def neto(self, neto):
        self.__neto = neto;


    def calcular_neto( self):         
        self.neto = self.importe+self.__monto_iva   
        
    # Montar el presupuesto     
    def montar_presupuesto(self):
        """Esta función se encarga de armar todo el presupuesto"""
        txt = '\n'+self.divline+'\n'
        txt += '\t'+self.encabezado_nombre+'\n'
        txt += '\tWeb Site: '+self.encabezado_web+' | '
        txt += 'E-mail: '+self.encabezado_email+'\n'
        txt += self.divline+'\n'
        txt += '\t'+self.titulo+'\n'
        txt += self.divline+'\n\n'
        txt += '\tFecha: '+self.fecha+'\n'
        txt += '\tEmpresa: '+self.empresa+'\n'
        txt += '\tCliente: '+self.cliente+'\n'
        txt += self.divline+"\n\n"
        txt += '\tDetalle del servicio:\n'
        txt += '\t'+self.servicio+'\n\n'
        txt += '\tImporte: €%0.2f | IVA: €%0.2f\n'% (self.importe, self.__monto_iva)         
        txt += '-'*80
        txt += '\n\tMONTO TOTAL: €%0.2f\n' % (self.neto)         
        txt += self.divline+'\n'
        print(txt)     


class Cliente:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre;
        self.__apellido = apellido;
    
    @property
    def nombre(self):
        return self.__nombre;
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre;

    @property
    def apellido(self):
        return self.__apellido;

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido;

    def __str__(self):
        sResultado = "";
        sResultado += "nombre: " + self.nombre();
        sResultado += "apellido: " + self.apellido();

        
