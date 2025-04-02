# Escritura de Archivo de Texto
# Creamos un archivo llamado "my_notes.txt" y escribimos tres líneas de notas personales.
with open("my_notes.txt", "w") as file:
    file.write(" ejercicio de escritura de texto en python.\n")
    file.write("Hoy he aprendido sobre manipulación de archivos en Python, es decir abrir escribir textos.\n")
    file.write("Cerrar archivos es una buena práctica para liberar recursos, tomando en cuenta que puede haber mas de un metos de cerrar archivos.\n")
    file.write("Es fundamental manejar este tema a perfeccion ya que permite manipular y trabajar con archivos sean estos grandes o pequeños \n")
    file.write("Soy estudiante de ingenieria en tecnologias de informacion \n")
    file.write(" Quiero especializarme en inteligencia artificial y la interaccion hombre- maquina \n")
    file.write(" Tengo afinidad por las matematicas y todo lo que tiene que ver con programacion \n")
    file.write("Espero terminar el semestre de la mejor manera posible para avanzar en mi carrera \n")

# No es necesario cerrar el archivo manualmente, ya que 'with open' lo maneja automáticamente.

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura y mostramos cada línea en la consola.
with open("my_notes.txt", "r") as file:
    print("Contenido del archivo:")
    for line in file:  # Leer línea por línea
        print(line.strip())  # Eliminamos los saltos de línea extra
# No es necesario cerrar el archivo manualmente, ya que 'with open' lo maneja automáticamente.

# dependiendo del archivo se puede cerrar el archivo de manera manual o automatica como lo estoy asiendo en este programa
