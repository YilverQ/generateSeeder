estructuraSeeder = "Institution::create(['name' => '{}']);"
text = ''

def convertir_a_mayusculas(texto):
    inicio_parentesis = texto.find("(")
    fin_parentesis = texto.find(")")
    
    if inicio_parentesis != -1 and fin_parentesis != -1:
        texto_parentesis = texto[inicio_parentesis+1:fin_parentesis]
        texto_mayusculas = texto[:inicio_parentesis+1] + texto_parentesis.upper() + texto[fin_parentesis:]
        return texto_mayusculas
    else:
        return texto


# Abrir el archivo de entrada en modo lectura
with open("Data.txt", "r") as archivo_entrada:
    # Abrir el archivo de salida en modo escritura
    with open("Seeder.txt", "w") as archivo_salida:
        # Leer cada línea del archivo de entrada
        for linea in archivo_entrada:
            # Guardar la línea leída en la variable text
            text = linea.strip()
            result = " ".join(word.capitalize() for word in text.split()) 
            result = convertir_a_mayusculas(result)
            # Escribir en el archivo de salida la estructuraSeeder con el texto correspondiente
            archivo_salida.write(estructuraSeeder.format(result) + "\n")