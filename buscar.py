#Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
#Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.
#Implementa una función que realice una búsqueda en la matriz para encontrar un valor específico que definas.
#Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
valor_buscar = int(input("Ingrese el valor a buscar en la matriz: "))
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición si encuentra el valor
    return None

# Valor a buscar

resultado = buscar_valor(matriz, valor_buscar)

# Mostrar resultado
if resultado:
    print(f"El valor {valor_buscar} se encontró en la posición {resultado}.")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")

