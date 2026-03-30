inventario = {}
id_actual = 1


def agregar_producto():
    global id_actual
    
    nombre = input("Nombre del producto: ").strip().lower()
    
    precio = float(input("Precio: ").strip())
    if precio <= 0:
        print("El precio debe ser positivo")
        return
    
    inventario[id_actual] = {
        "nombre": nombre,
        "precio": precio
    }
    
    print("Producto agregado con ID:", id_actual)
    
    id_actual += 1


def mostrar_productos():
    if len(inventario) == 0:
        print("Inventario vacío")
        return
    
    print("\nInventario:")
    for id_producto, datos in inventario.items():
        print("ID:", id_producto, "|", datos["nombre"], "-", datos["precio"])


def actualizar_producto():
    id_producto = int(input("Ingrese el ID del producto: ").strip())
    
    if id_producto not in inventario:
        print("El producto no existe")
        return
    
    nuevo_precio = float(input("Nuevo precio: ").strip())
    
    if nuevo_precio <= 0:
        print("Precio inválido")
        return
    
    inventario[id_producto]["precio"] = nuevo_precio
    print("Producto actualizado")


def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto: ").strip())
    
    if id_producto not in inventario:
        print("El producto no existe")
        return
    
    del inventario[id_producto]
    print("Producto eliminado")


def menu():
    opcion = ""
    
    while opcion != "5":
        print(" \n____ MENU ____")
        print("\n 1. Agregar\n 2. Mostrar\n 3. Actualizar\n 4. Eliminar\n 5. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Saliendo...")
        else:
            print("Opción inválida")


menu()
