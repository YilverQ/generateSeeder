# Abre el archivo de texto en modo lectura
with open('Data.txt', 'r') as archivo:
    # Lee todas las líneas del archivo y guárdalas en una lista
    lineas = archivo.readlines()

# Ordena la lista alfabéticamente
lineas_ordenadas = sorted(lineas)

# Imprime o guarda en otro archivo el resultado ordenado
for linea in lineas_ordenadas:
    print(linea.strip())  # strip() elimina los saltos de línea al final de cada línea

# También puedes guardar el resultado en otro archivo
with open('Data.txt', 'w') as archivo_ordenado:
    for linea in lineas_ordenadas:
        archivo_ordenado.write(linea)