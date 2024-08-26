# Solicitar el ingreso de los elementos del arreglo
arreglo = list(map(int, input("Ingresa los números del arreglo separados por espacios: ").split()))

# Separar los elementos que no son cero
no_ceros = [num for num in arreglo if num != 0]

# Contar la cantidad de ceros en el arreglo
cantidad_ceros = arreglo.count(0)

# Crear el nuevo arreglo con los no ceros seguidos por los ceros
arreglo_final = no_ceros + [0] * cantidad_ceros

# Mostrar el resultado
print(f"El arreglo con los ceros al final es: {arreglo_final}")