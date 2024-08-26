# Solicitar el ingreso de los elementos del arreglo
# Convertimos la entrada en una lista de números flotantes (reales)
arreglo_reales = list(map(float, input("Ingresa los números reales separados por espacios: ").split()))

# Calcular la suma de los elementos del arreglo
suma = sum(arreglo_reales)

# Calcular el promedio
promedio = suma / len(arreglo_reales)

# Mostrar el resultado
print(f"El promedio del arreglo es: {promedio}")