cuentas = [(300,450), (400,300), (500,350), (450,300)]
# el primer numero indica ingresos, el segundao gastos.
impares = cuentas[::3]
pares = cuentas[::2]
dosPrimeros = cuentas[:2]
dosUltimos = cuentas[2:]
primeroYultimo = cuentas[0], cuentas[3]
print(primeroYultimo)