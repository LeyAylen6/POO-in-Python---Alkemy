# 2. Crear una lista con 5 elementos y luego aplica los siguientes
# accionables:
# ↪ Imprimir el último elemento
# ↪ Modificar el valor del tercer elemento
# ↪ Agregar dos elementos
# ↪ Eliminar algún elemento

list = ["the one", 2, 3, 4, 5]

print(list[4])
list[2] = "I'm changed"
list.append("I'm the first new")
list.append("I'm the second new")
list.remove("the one")

print(list)