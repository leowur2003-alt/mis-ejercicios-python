archivo = input("Introduce la ruta del archivo de texto: ")
try:
    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print("El archivo especificado no existe")
    exit(1)
# Separar el contenido en palabras
import re
palabras = re.findall(r"\w+", texto.lower())
total_palabras = len(palabras)
print(f"Total palabras: {total_palabras}")
from collections import Counter
mas_comunes = Counter(palabras).most_common(10)
print("Palabras más frecuentes:")
for palabra, freq in mas_comunes:
        print(f"{palabra}: {freq}")