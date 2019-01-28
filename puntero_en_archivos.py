from io import *

archivo_de_texto = open("texto.txt","r")

# el metodo seek dispone de un parametro que es el numero de caracter donde posicionarse el puntero:

archivo_de_texto.seek(38)

print(archivo_de_texto.read())
print("-------------------------")

# colocamos el puntero al principio:

archivo_de_texto.seek(0)

print(archivo_de_texto.read())
print("-------------------------")

# el metodo "read" dispone de un parametro limite de lectura. podemos indicarle
# que pare de leer a la altura del caracter que indiquemos:

archivo_de_texto.seek(0)

print(archivo_de_texto.read(37))
print("-------------------------")

# si realizamos otra lectura leera desde el punto de detenccion:
print(archivo_de_texto.read())
print("-------------------------")
# podemos operar con otros metodos con estas instrucciones. 
#por ejemplo conocer el tamano de un archivo de texto con el metodo "len"

archivo_de_texto.seek(0)
print(len(archivo_de_texto.read()))
# y almacenarlo en una variable para operar con ella.
archivo_de_texto.seek(0)
tamano = len(archivo_de_texto.read())
print("-------------------------")
mitad = tamano / 2
print(mitad)
print("-------------------------")
archivo_de_texto.seek(0)
# se puede colocar el puntero al final de la primera linea con la instruccion "readline"
archivo_de_texto.seek(len(archivo_de_texto.readline()))
print(archivo_de_texto.read())
print("-------------------------")

