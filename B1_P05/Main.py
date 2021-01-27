from B1_P05.Agenda import Agenda
from B1_P05.Persona import Persona

agenda = []
a = Agenda(agenda)

nombre = input("Nombre: " )
apellido = input("Apellido: " )
p = Persona(nombre, apellido, "646000204")

#a.guardarEnTXT(p)

a.borrar(nombre, apellido)

print(a.buscar(nombre, apellido))

#a.leertxt()