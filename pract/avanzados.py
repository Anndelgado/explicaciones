def pedir_nombre():
    nombre = ""
    while nombre == "":
        nombre = input("Nombre del producto: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío")
    return nombre


def pedir_precio():
    precio = -1
    while precio <= 0:
        precio = float(input("Precio: "))
        if precio <= 0:
            print("El precio debe ser mayor a 0")
    return precio


def pedir_continuar():
    continuar = ""
    while continuar != "si" and continuar != "no":
        continuar = input("¿Desea continuar? (si/no): ").lower().strip()
        if continuar != "si" and continuar != "no":
            print("Solo puedes escribir 'si' o 'no'")
    return continuar


def main():
    productos = []  # lista de diccionarios
    
    continuar = "si"
    
    while continuar == "si":
        nombre = pedir_nombre()
        precio = pedir_precio()
        
        producto = {
            "nombre": nombre,
            "precio": precio
        }
        
        productos.append(producto)
        
        continuar = pedir_continuar()
    
    # Procesamiento
    total = 0
    mayor = productos[0]
    menor = productos[0]
    
    for producto in productos:
        total += producto["precio"]
        
        if producto["precio"] > mayor["precio"]:
            mayor = producto
        
        if producto["precio"] < menor["precio"]:
            menor = producto
    
    promedio = total / len(productos)
    
    # Resultados
    print("Total:", total)
    print("Promedio:", promedio)
    print("Más caro:", mayor["nombre"], "-", mayor["precio"])
    print("Más barato:", menor["nombre"], "-", menor["precio"])


main()