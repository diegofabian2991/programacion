def calcular_temperatura_promedio(temperaturas): # definimos la funcion
    promedios = {}

    for ciudad, semanas in temperaturas.items():  # Iteramos por cada ciudad en el diccionario de temperaturas
        suma_temperaturas = 0

        for temp in semanas: # Iteramos por las semanas de la ciudad
            suma_temperaturas += temp  # Sumar las temperaturas semana a semana

        # Calculamos el promedio de la ciudad
        promedio_ciudad = suma_temperaturas / len(semanas)
        promedios[ciudad] = promedio_ciudad

    return promedios

# Datos de temperaturas de las ciudades durante 4 semanas
temperaturas = {
    "CiudadA": [23, 25, 22, 24],  # Temperaturas para 4 semanas
    "CiudadB": [30, 32, 31, 33],  # Temperaturas para 4 semanas
    "CiudadC": [18, 20, 19, 21],  # Temperaturas para 4 semanas
    "CiudadD": [12, 27, 10, 23],  # Temperaturas para 4 semanas
    "CiudadE": [17, 26, 17, 20],  # Temperaturas para 4 semanas
    "CiudadF": [32, 25, 14, 29],  # Temperaturas para 4 semanas
    "CiudadG": [10, 24, 13, 24],  # Temperaturas para 4 semanas
    "CiudadH": [18, 23, 23, 25],  # Temperaturas para 4 semanas
    "CiudadI": [13, 22, 30, 26]   # Temperaturas para 4 semanas
}

#Llamamos a la función para calcular el promedio
promedios = calcular_temperatura_promedio(temperaturas)

# Mostramos los promedios
for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio:.2f}°C")
