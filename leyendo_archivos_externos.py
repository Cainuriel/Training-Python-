from io import *
# el modo de este archivo sera solo de lectura. en ese caso la palabra r en vez de w o a:
archivo_de_texto = open("texto.txt","r")

#creamos una variable para almacenar el texto del archivo y el metodo de lectura "read":

lectura_archivo = archivo_de_texto.read()

# no olvidar cerrar el archivo abierto en memoria.
archivo_de_texto.close()

print(lectura_archivo)

# el metodo readlines almacena las lineas de texto en una lista.

archivo_de_texto = open("pruebas_lectura.txt","r")

lineasdetexto = archivo_de_texto.readlines()

archivo_de_texto.close()

# si imprimimos la variable comprobaremos que es una lista:
print(lineasdetexto)

# para acceder a una linea concreta del documento de texto, tratarlas como elementos de una lista:

print(lineasdetexto[1])


