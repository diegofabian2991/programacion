# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para representar una segunda profesion
informacion_personal["profesion_secundaria"] = "Profesor"

# Verificar si la clave "telefono" existe en el diccionario, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad")

# Imprimir el diccionario final
print(informacion_personal)
