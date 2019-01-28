from io import *
# importamos el modulo io que incluye metodos para trabajar con archivos externos.

# utilizaremos el metodo OPEN para crear un archivo de texto. posee dos argumentos:
# 1. el nombre del archivo.
# 2. modo de apertura del archivo. tres modos:
# MODO LECTURA "r", MODO ESCRITURA "w" Y MODO APPEND "a": "Sobre-escribir en un archivo ya creado" 
# el ejemplo lo crearemos en modo escritura:

archivo_de_texto = open("texto.txt","w")

frase = "Hay que ver lo que me cuesta estudiar. \n Pero la verdad, es que me gusta mucho la informatica."

# metodo de escritura. introducimos la frase en el archivo creado.
archivo_de_texto.write(frase)

# despues de escribir, hay que cerrar el archivo abierto en memoria, con el anterior metodo "open".
archivo_de_texto.close()

# vamos a manipular el texto con el metodo append, usando la palabra "a":

archivo_de_texto = open("texto.txt","a")

# escribimos usando el metodo"write"

archivo_de_texto.write("\n Y si me gusta tendre que estudiar mas")

archivo_de_texto.close()
# para borrar de la memoria el archivo:
del(archivo_de_texto)

