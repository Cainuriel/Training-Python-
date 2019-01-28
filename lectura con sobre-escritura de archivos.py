from io import *

# con el modo "r+" determinamos el modo lectura y escritura a la vez:

archivo = open("texto.txt","r+")

# si ahora escribimos sin colocar el puntero sobre-escribiremos.
# para evitarlo comprobamos la longitud del texto y colocamos el cursor al final + 1:

finaltexto = len(archivo.read())

# colocamos el puntero al final:
archivo.seek(finaltexto+1)
# ahora no borraremos texto:
archivo.write("\n Prueba de sobre escritura al final del documento")

archivo.seek(0)
print(archivo.read())

# vamos a introducir una linea en medio del texto. 
#primeramente guardaremos el texto en una lista
archivo.seek(0)
lista = archivo.readlines()
# comprobamos las lineas guardadas en la lista
print(lista)
# ahora colocaremos una linea antes de la linea de sobre escritura
lista[3] = "Esta linea es un intruso antes de la ultima linea \n"
archivo.seek(0)
# el metodo "writelines" introduce lineas con una lista
archivo.writelines(lista)
archivo.seek(0)
print(archivo.read())
archivo.close()
