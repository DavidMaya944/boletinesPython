from B1_P05.Agenda import Agenda
from B1_P05.Persona import Persona

agenda = []
a = Agenda(agenda)
p = Persona("David", "Maya", "646000204")

a.guardarEnTXT(p)

a.leertxt()