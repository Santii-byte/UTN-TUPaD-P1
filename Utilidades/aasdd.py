# Crear una matriz vacía
matriz = []

# Rellenar la matriz
for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Imprimir la matriz
print("\nMatriz 3x3:")
for fila in matriz:
    print(fila)

for i in range(3):
    lista = []
    for j in range(3):
        lista.append(matriz[i][j])
    promedio=0
    for k in range(len(lista)):
        promedio+=lista[k]
    promedio=promedio/len(lista)
    print(f"Promedio de la fila {i}: {promedio}")