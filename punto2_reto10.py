# Solicitar el ingreso los elementos del primer arreglo
arreglo1 = list(map(float, input("Ingresa los números del primer arreglo separados por espacios: ").split()))

# Solicitar el ingreso los elementos del segundo arreglo
arreglo2 = list(map(float, input("Ingresa los números del segundo arreglo separados por espacios: ").split()))

# Verificar que ambos arreglos tengan el mismo tamaño
if len(arreglo1) != len(arreglo2):
    print("Error: Los arreglos deben tener el mismo tamaño.")
else:
    # Calcular el producto punto
    producto_punto = sum(a * b for a, b in zip(arreglo1, arreglo2))
    
    # Mostrar el resultado
    print(f"El producto punto de los arreglos es: {producto_punto}")