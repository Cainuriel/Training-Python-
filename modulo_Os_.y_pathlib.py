"""
Modulo para crear y getionar archivos
"""

import os

#crear directorio, sino existe.
os.makedirs("./Creandodirectorios/Conelmodulo_Os/",exist_ok = True)

# el punto nos indica el directorio actual. 
archivos_carpeta_actual = os.listdir(".")
print("""
	estos son los archivos que hay en la carpeta actual""",archivos_carpeta_actual)

# crando archivo de texto. si ya esta creado sobre-escribira.
archivo_para_escribir = open("./Creandodirectorios/Conelmodulo_Os/holamundo.txt","w")
archivo_para_escribir.write("Hola ")
archivo_para_escribir.write("Mundo ")
archivo_para_escribir.close()

# para no borrar el contenido, seleccionar la "a" de append: añadir.
archivo_para_escribir = open("./Creandodirectorios/Conelmodulo_Os/holamundo.txt","a")
archivo_para_escribir.write("Esto está ")
archivo_para_escribir.write(" añadido. ")
archivo_para_escribir.close()



""" la forma adecuada de abrir y escribir es con el contexto with
que supuestamente, garantiza que toda la operación se realice
su sintaxys es la siguiente
"""
lista = ["Fernando lopez ","Manuel Hermida", "Cristina campos ","Luis Gutierrez"]
with open("./Creandodirectorios/Conelmodulo_Os/holamundo.txt","a") as archivo_with:
	archivo_with.write("\n")
	for l in lista:
		archivo_with.write(l)
		archivo_with.write("\n")

# no es necesario poner "r". Es por defecto. 
with open("./Creandodirectorios/Conelmodulo_Os/holamundo.txt") as archivo_with:
	archivo_para_leer = archivo_with.read()
print(archivo_para_leer)

# meter texto en una lista
datosdeltexto = []
with open("./Creandodirectorios/Conelmodulo_Os/holamundo.txt") as archivo_with:
	archivo_para_leer = archivo_with.readlines()
	for datos in archivo_para_leer:
		# borramos el salto de linea.
		datosdeltexto.append(datos.strip("\n"))
print(datosdeltexto)


"""
la libreria pathlib nos ahorra toda la problematica de lectura de archivos en
diferentes sistemas operativos, por culpa de la diferente escritura de los
path, veamoslo.
"""
from pathlib import Path

# comodo uso de los archivos.
carpeta = Path("./Creandodirectorios/Conelmodulo_Os")

archivo = carpeta / "holamundo.txt"

print(type(archivo))

print(archivo.read_text())

# creando archivos de forma sencilla.
archivo_creado_conpathlib = carpeta / "holamundodesdepathlib.txt"
archivo_creado_conpathlib.write_text("Esto esta escrito usando la libreria pathlib")

# para meter una lista tenemos que usar el "with"
# pero con el objeto "archivo" creado con pathlib
with open(archivo_creado_conpathlib,"a") as archivo_with:
	archivo_with.write("\n")
	for l in lista:
		archivo_with.write(l)
		archivo_with.write("\n")

print(archivo_creado_conpathlib.read_text())

