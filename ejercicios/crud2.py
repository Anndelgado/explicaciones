usuarios = {}
id_actual = 1

def agregar_usuario():
    global id_actual
    
    nombre = input("Ingrese el nombre: ").strip().lower()
    edad = int(input("Ingrese edad: ").strip())
    
    if nombre == "":
        print("El nombre no puede estar vacío")
        return
    
    if edad <= 0:
        print("Edad invalida!")
        return
    
    usuarios[id_actual]={
        "nombre": nombre,
        "edad": edad
    }
    
    print("Usuario agregado con el ID: ", id_actual)
    id_actual += 1
    
def mostrar_usuarios():
    if len(usuarios) == 0:
        print("Base de datos de usuarios vacio.")
        return
    print("\n Usuarios: ")
    for id_usuarios, datos in usuarios.items():
        print("ID:", id_usuarios, "|", "Nombre: ", datos["nombre"], "-", "Edad: ", datos["edad"])
            
def actualizar_usuarios():
    print("¿Que deseas actualizar?\n")
    print(" 1. Actualizar nombre\n 2. Actualizar edad")
        
    opcion = input("Elige una opción: ").strip()
        
    if opcion not in ["1", "2"]:
        print("Ingresa una opción valida.")
        return
        
    if opcion == "1":         
        id_usuario =  int(input("Ingrese el ID del usuario: ").strip())
        
        if id_usuario not in usuarios:
            print("Usuario no encontrado.")
            return
            
        nuevo_nombre = input("Cambio de nombre: ").strip()
            
        if nuevo_nombre == "":
            print("No se permiten espacios en blanco.")
                
        usuarios[id_usuario]["nombre"] = nuevo_nombre
        print("Nombre actualizado")
        
    if opcion == "2":         
        id_usuario =  int(input("Ingrese el ID del usuario: ").strip())
        
        if id_usuario not in usuarios:
            print("Usuario no encontrado.")
            return
            
        nuevo_edad = int(input("Nueva edad: ").strip())
    
        if nuevo_edad <= 0:
            print("Edad inválida")
            return
        usuarios[id_usuario]["edad"] = nuevo_edad
        print("Edad actualizada")

def eliminar_usuario():
    id_usuario = int(input("Ingrese el ID del usuario: ").strip())
    
    if id_usuario not in usuarios:
        print("Usuario no existe")
        return
    
    del usuarios[id_usuario]
    print("Usuario eliminado")
    
def menu():
    opcion = ""
    
    while opcion != "5":
        print(" \n____ MENU ____")
        print("\n 1. Agregar usuario\n 2. Mostrar usuario\n 3. Actualizar datos de usuario\n 4. Eliminar usuario\n 5. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            actualizar_usuarios()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            print("Saliendo...")
        else:
            print("Opción inválida")


menu()




    
        
            
    
    
    
    