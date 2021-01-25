import sqlite3

# Crear conexión
conn = sqlite3.connect('mydatabase.db')

# Obtener cursor
cursor = conn.cursor()

# Ejecutar sentencia de creacion de tabla
cursor.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, salary real)")
conn.commit()



# Ejecutar sentencia de inserccion
cursor.execute("INSERT INTO employees VALUES(2, 'John', 700)")
cursor.execute("INSERT INTO employees VALUES(3, 'Mike', 800)")
cursor.execute("INSERT INTO employees VALUES(4, 'Denzel', 650)")
conn.commit()

# Recorriendo las filas devueltas por fetchall
cursor.execute('SELECT id, name FROM employees')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Recorriendo fila a fila con fetchore
cursor.execute('SELECT id, name FROM employees')
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

# Usando el cursor como un iterador
cursor.execute('SELECT id name FROM employees')
for row in cursor:
    print(row)

conn.commit()