'''EJERCICIO 1 (básico pero importante)

Un programa debe pedir números al usuario hasta que ingrese un número negativo.
Al final, mostrar:

La suma de los números
Cuántos números ingresó
'''
'''
suma_final = 0
contador = 0
numero = 0


while numero >= 0:
    numero = int(input("Ingresa un número: ").strip())
    
    if numero >= 0:
        suma_final += numero
        contador += 1
        
        
        
print("Suma:", suma_final)
print("Cantidad:", contador)


'''

'''
EJERCICIO 2 (intermedio)

Un sistema pide al usuario ingresar varios números.
El programa debe:

Determinar el número mayor
Determinar el número menor
Calcular el promedio

El usuario decide cuándo dejar de ingresar números.

'''
'''
suma_final = 0
contador = 0
continuar = "si"

while continuar == "si":
    numero = int(input("Ingresa un número: ").strip())
    
    
    if contador == 0:
       mayor = numero
       menor = numero
       
    suma_final += numero
    contador += 1      
     
    if numero > mayor:
        mayor = numero

    if numero < menor:
        menor = numero
        
    continuar = input("¿Desea continuar? (si/no): ").lower().strip()
       
promedio = suma_final / contador

print("Mayor:", mayor)
print("Menor:", menor)
print("Promedio:", promedio)        
'''
'''
EJERCICIO 3 (tipo examen )

Un sistema de tienda registra ventas.
Por cada venta se ingresa:

Nombre del producto
Precio

El programa debe permitir múltiples productos y al final mostrar:

Total de la compra
Promedio de precios
Producto más barato
Producto más caro
'''
total = 0
contador = 0
continuar = "si"

while continuar == "si":
    
    # Validar nombre
    nombre = ""
    while nombre == "":
        nombre = input("Nombre del producto: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío")
    
    # Validar precio
    precio = -1
    while precio <= 0:
        precio = float(input("Precio: "))
        if precio <= 0:
            print("El precio debe ser mayor a 0")
    
    # Primer producto
    if contador == 0:
        mayor_precio = precio
        nombre_mayor = nombre
        menor_precio = precio
        nombre_menor = nombre
    
    # Acumuladores
    total += precio
    contador += 1
    
    # Producto más caro
    if precio > mayor_precio:
        mayor_precio = precio
        nombre_mayor = nombre
    
    # Producto más barato
    if precio < menor_precio:
        menor_precio = precio
        nombre_menor = nombre
    
    # Validar continuar
    continuar = ""
    while continuar != "si" and continuar != "no":
        continuar = input("¿Desea continuar? (si/no): ").lower().strip()
        if continuar != "si" and continuar != "no":
            print("Solo puedes escribir 'si' o 'no'")

# Promedio
promedio = total / contador

# Resultados
print("Total de la compra:", total)
print("Promedio de precios:", promedio)
print("Producto más caro:", nombre_mayor, "-", mayor_precio)
print("Producto más barato:", nombre_menor, "-", menor_precio)