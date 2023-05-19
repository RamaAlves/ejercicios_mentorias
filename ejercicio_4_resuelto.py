""" Crear una funcion que reciba un numero 'x' e imprima los primeros 'x' números de la sucesión de Fibonacci."""

def fibonacci(x):
    # Casos base
    if x <= 0:
        return []
    elif x == 1:
        return [0]
    elif x == 2:
        return [0, 1]
    
    secuencia = [0, 1]  # Almacenamos la secuencia de Fibonacci
    
    # Generamos la secuencia de Fibonacci
    while len(secuencia) < x:
        numero_siguiente = secuencia[-1] + secuencia[-2]  # Calculamos el siguiente número de Fibonacci
        secuencia.append(numero_siguiente)
    
    return secuencia

# Ejemplo de uso
numero = int(input("Ingrese la cantidad de números de Fibonacci que desea imprimir: "))
numeros_fib = fibonacci(numero)

print("La secuencia de Fibonacci de longitud", numero, "es:")
for num in numeros_fib:
    print(num)