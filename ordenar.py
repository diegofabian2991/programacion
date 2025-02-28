
matriz = [
    [9, 3, 7],
    [5, 1, 4],
    [8, 6, 2]
]
fila_a_ordenar = int(input("Ingrese el número de la fila a ordenar (0, 1 o 2): "))

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:  # Intercambia si el elemento es mayor que el siguiente
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Matriz de ejemplo (3x3)


print("Matriz original:")
mostrar_matriz(matriz)

# Selección de fila a ordenar


if 0 <= fila_a_ordenar < len(matriz):  # Verifica que la fila sea válida
    bubble_sort(matriz[fila_a_ordenar])  # Ordena la fila seleccionada

    print("\nMatriz después de ordenar la fila:")
    mostrar_matriz(matriz)
else:
    print("Número de fila inválido. Debe ser 0, 1 o 2.")