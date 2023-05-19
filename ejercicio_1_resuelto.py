""" Conversor de unidades: Desarrolla un programa que convierta unidades de medida, 
como kilómetros a millas, grados Celsius a Fahrenheit o libras a kilogramos. 
Puedes permitir al usuario ingresar los valores a convertir. """


def kilometros_a_millas(kilometros):
    millas = kilometros * 0.621371
    return millas

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def libras_a_kilogramos(libras):
    kilogramos = libras * 0.453592
    return kilogramos

print("¡Bienvenido al conversor de unidades!")

while True:
    print("\nSelecciona una opción:")
    print("1. Kilómetros a Millas")
    print("2. Grados Celsius a Fahrenheit")
    print("3. Libras a Kilogramos")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción que desea realizar: ")

    if opcion == "4":
        print("¡Hasta luego!")
        break

    if opcion == "1":
        kilometros = float(input("Ingrese la cantidad de kilómetros: "))
        millas = kilometros_a_millas(kilometros)
        print(kilometros, "kilómetros equivalen a", millas, "millas.")
    elif opcion == "2":
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(celsius, "grados Celsius equivalen a", fahrenheit, "grados Fahrenheit.")
    elif opcion == "3":
        libras = float(input("Ingrese la cantidad de libras: "))
        kilogramos = libras_a_kilogramos(libras)
        print(libras, "libras equivalen a", kilogramos, "kilogramos.")
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")