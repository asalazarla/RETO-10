# RETO-10

***Este repositorio contiene la solución y desarrollo a los problemas del reto 10***

**1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.**

```python
# Solicitar el ingreso de los elementos del arreglo
# Convertimos la entrada en una lista de números flotantes (reales)
arreglo_reales = list(map(float, input("Ingresa los números reales separados por espacios: ").split()))

# Calcular la suma de los elementos del arreglo
suma = sum(arreglo_reales)

# Calcular el promedio
promedio = suma / len(arreglo_reales)

# Mostrar el resultado
print(f"El promedio del arreglo es: {promedio}")
```

**2. Desarrollar un algoritmo que calcule el [producto punto](https://www.cuemath.com/algebra/dot-product/)**

```python
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
```

**3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.**

```python
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
```

**4. Revisar que son los algoritmos de *sorting*, entender *bubble-sort* ([enlace](https://www.geeksforgeeks.org/bubble-sort/) a implementación).

Para este numeral no se realizó ningún code, ya que su principal objetivo es entender algoritmos de sorting que son métodos para organizar los elementos de una lista en un orden específico, como ascendente o descendente. 
Además también se pide la comprensión de bubble-sort que se caracteriza por ser un algoritmo sencillo que compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que la lista está ordenada. (Describí brevemente lo que entendí) 

