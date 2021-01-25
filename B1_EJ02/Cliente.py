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
