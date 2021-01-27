from B1_P05.Agenda import Agenda
from B1_P05.Persona import Persona

agenda = []
a = Agenda(agenda)

nombre = input("Nombre: " )
apellido = input("Apellido: " )
telefono = input("Telefono: ")

p = Persona(nombre, apellido, telefono)

a.meterEnArray(p)

a.meterEnFichero()

a.cargarFichero()

a.imprimirArray()