# 1. Declaración de variables
nombre = "Juan"
edad = 20
notas = [85, 90, 78, 92, 88]  # Asignación de valores a variables

# 2. Comandos de control de flujo de programa
# Uso de 'if' para verificar si es mayor de edad
if edad >= 18:
    print(nombre, "es mayor de edad.")
else:
    print(nombre, "es menor de edad.")

# Uso de 'for' para recorrer la lista de notas
print("Listado de notas:")
for nota in notas:
    print(nota)

# 3. Lectura de archivos y asignación a vectores y tablas
import os
import re
import matplotlib.pyplot as plt

# Definir la ruta relativa del archivo
ruta_archivo = os.path.join('src', 'data', 'ejemplo.txt')

# Leer el contenido del archivo
try:
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print(f"El archivo '{ruta_archivo}' no existe. Verifica la ruta y el nombre del archivo.")
    contenido = ""

# Procesar el contenido: convertir a minúsculas y extraer palabras usando expresiones regulares
palabras = re.findall(r'\w+', contenido.lower())

# 4. Asignación de valores a variables (frecuencia de palabras)
frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, frec in frecuencias.items():
    print(f"{palabra}: {frec}")

# 5. Gráfica de frecuencias
# Graficar las 10 palabras más frecuentes
palabras_ordenadas = sorted(frecuencias, key=frecuencias.get, reverse=True)[:10]
frecuencias_ordenadas = [frecuencias[p] for p in palabras_ordenadas]

plt.bar(palabras_ordenadas, frecuencias_ordenadas, color='skyblue')
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.title("Frecuencia de palabras (Top 10)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Escritura de archivos texto
# Escribir la tabla de frecuencias en un archivo de salida
ruta_salida = os.path.join('src', 'data', 'salida.txt')
with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.write("Tabla de frecuencia de palabras:\n")
    for palabra, frec in frecuencias.items():
        archivo_salida.write(f"{palabra}: {frec}\n")

print(f"Evidencia generada en el archivo '{ruta_salida}'.")