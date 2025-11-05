# 1) Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("Ingresa un número para calcular los factoriales hasta ese valor: "))
print(f"\nFactoriales del 1 al {numero}:")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")


# 2) Serie de Fibonacci recursiva
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


posicion = int(input("\nIngresa hasta qué posición de Fibonacci deseas mostrar: "))
print(f"Serie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion):
    print(fibonacci(i), end=" ")
print()  # salto de línea


# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


base = int(input("\nIngresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")


# 4) Conversión decimal a binario recursiva
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


numero_decimal = int(input("\nIngresa un número decimal positivo: "))
binario = decimal_a_binario(numero_decimal)
print(f"El número {numero_decimal} en binario es: {binario}")


# 5) Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])


palabra = input("\nIngresa una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")


# 6) Sumar los dígitos de un número
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


numero = int(input("\nIngresa un número entero positivo para sumar sus dígitos: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")


# 7) Contar bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


niveles = int(input("\nIngresa el número de bloques del nivel más bajo de la pirámide: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")


# 8) Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


numero = int(input("\nIngresa un número entero positivo: "))
digito = int(input("Ingresa el dígito que deseas contar (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.")
