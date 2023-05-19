""" Mini gestor de contactos: Crea un programa que permita al usuario agregar, 
eliminar y buscar contactos en una lista. 
Puedes almacenar los contactos en un diccionario con nombres y números de teléfono. """

def agregar_contacto(agenda, nombre, telefono):
    """ recibe un diccionario, el nombre del contacto de
        y el numero de telefono. Verifica si el contacto existe
        si no existe lo agrega al diccionario
    """
    #...

def eliminar_contacto(agenda, nombre):
    """ recibe un diccionario y un nombre.
        busca si el nombre existe en el diccionario
        y si lo encuentra lo elimina
    """
    #...

def buscar_contacto(agenda, nombre):
    """ recibe un diccionario y un nombre
        si encuentra el nombre en la agenda 
        muestra la informacion del contacto
    """
    #...

agenda = {}

print("¡Bienvenido a la agenda de contactos!")

while True:
    print("\nSelecciona una opción:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "4":
        print("¡Hasta luego!")
        break

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agregar_contacto(agenda, nombre, telefono)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        eliminar_contacto(agenda, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        buscar_contacto(agenda, nombre)
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")