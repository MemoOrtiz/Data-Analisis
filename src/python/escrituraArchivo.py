import os

def crear_archivo_texto():
    carpeta = "src/data"        #alternativo: usa '../data' 
    nombre_archivo = "Big Data.txt"

    #ruta 
    ruta_archivo = os.path.join(carpeta, nombre_archivo)
    print(ruta_archivo)

    #Se crea la carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    #se abre o crea si no existe el archivo de texto, en modo escritura y sobre escribe el contenido
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("Este es un ejemplo pa la clase de Big Data.\n")
        archivo.write("Si ejecutas este archivo desde la raiz del proyecto siguiendo la estructura que tengo,\n")
        archivo.write("El archivo necesitará en la ruta src/data, pero si quieres ejecutarlo desde el equivalente de src.\n")
        archivo.write("Deberás cambiar la ruta de la carpeta en la variable 'carpeta' a '../data'.\n")
        archivo.write("Espero que haya sido de ayuda.\n")





"""
def leer_archivo_texto():
    carpeta = "src/data" #puede usar '../data' si se encuentra en src/python
    nombre_archivo = "ejemplo.txt"
    ruta_archivo = os.path.join(carpeta, nombre_archivo)

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        print("Contenido del archivo:\n")
        print(contenido)
    else:
        print(f"No se encontró el archivo en la ruta: {ruta_archivo}")
"""
if __name__ == "__main__":
    crear_archivo_texto()
    #leer_archivo_texto()