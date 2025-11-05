import math

# 1. Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")


# 2. Saludar al usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4. Calcular área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# 5. Convertir segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600


# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return suma, resta, multiplicacion, division


# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# 10. Calcular promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3


# PROGRAMA PRINCIPAL

# 1
imprimir_hola_mundo()

# 2
nombre_usuario = input("\nIngresa tu nombre: ")
print(saludar_usuario(nombre_usuario))

# 3
nombre = input("\nIngresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
radio = float(input("\nIngresa el radio del círculo: "))
print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")

# 5
segundos = float(input("\nIngresa la cantidad de segundos: "))
print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")

# 6
numero = int(input("\nIngresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7
a = float(input("\nIngresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
suma, resta, mult, div = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

# 8
peso = float(input("\nIngresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# 9
celsius = float(input("\nIngresa la temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10
n1 = float(input("\nIngresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio de los tres números es: {promedio:.2f}")
