cuentas = {"sevilla" : [300,450], "madrid" : [400,300], "segovia" : [500,350]
, "valencia" : [450,300]} # el primer numero indica ingresos, el segundo gastos.

cuentasMadridYSegovia = cuentas["madrid"], cuentas["segovia"]

cuentas["sevilla"] = cuentas["sevilla"] + [True]

sumaIngresos = 0
for x in cuentas.values():
    sumaIngresos += x[0]
    print(sumaIngresos)