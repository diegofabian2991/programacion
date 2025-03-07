# Datos de ejemplo (temperaturas en grados Celsius)
temperaturas = [[[22, 24, 25, 23], [21, 23, 22, 24], [22, 21, 23, 22], [23, 24, 23, 22], [24, 22, 24, 23],
                 [23, 23, 22, 24], [22, 21, 22, 23]],  # Ciudad 1
                [[28, 30, 32, 29], [29, 30, 31, 32], [30, 31, 30, 29], [28, 29, 28, 30], [29, 30, 32, 31],
                 [30, 29, 31, 30], [31, 30, 32, 31]],  # Ciudad 2
                [[15, 17, 16, 16], [16, 18, 17, 15], [17, 18, 19, 17], [18, 17, 18, 16], [17, 16, 17, 18],
                 [18, 16, 17, 19], [16, 17, 15, 17]],  # Ciudad 3
                [[17, 17, 14, 13], [15, 16, 17, 15], [10, 11, 14, 13], [18, 18, 17, 17], [17, 16, 10, 9],
                 [20, 16, 12, 19], [16, 12, 13, 15]],  # Ciudad 4
                [[11, 12, 13, 14], [16, 18, 17, 15], [17, 18, 10, 17], [12, 17, 18, 16], [17, 16, 17, 18],
                 [28, 26, 27, 9], [16, 17, 15, 17]],  # Ciudad 5
                [[15, 17, 16, 16], [16, 18, 17, 15], [17, 18, 19, 17], [17, 10, 28, 16], [17, 16, 17, 18],
                 [18, 16, 17, 19], [16, 17, 15, 17]],  # Ciudad 6
                [[15, 17, 16, 36], [16, 18, 17, 25], [17, 18, 29, 27], [18, 17, 18, 26], [17, 16, 17, 18],
                 [18, 16, 17, 19], [16, 17, 15, 17]],  # Ciudad 7
                [[15, 27, 26, 36], [16, 18, 17, 15], [17, 18, 19, 17], [18, 37, 28, 16], [17, 36, 17, 18],
                 [18, 19, 17, 29], [26, 17, 25, 17]]]  # Ciudad 8

# Número de ciudades, días y semanas
ciudades = 8  # Cambié de 7 a 8 para que coincida con los datos proporcionados
dias = 7
semanas = 4

# Iterar sobre las ciudades y las semanas para calcular el promedio
for ciudad in range(ciudades):
    print(f"\nPromedio de temperaturas para la Ciudad {ciudad + 1}:")

    for semana in range(semanas):
        suma_temperaturas = 0

        # Sumar las temperaturas de los 7 días de la semana para una ciudad en una semana
        for dia in range(dias):
            suma_temperaturas += temperaturas[ciudad][dia][semana]

        # Calcular el promedio
        promedio = suma_temperaturas / dias
        print(f"Semana {semana + 1}: {promedio:.2f}°C")