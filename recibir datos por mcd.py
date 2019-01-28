import sys

# la lista que genera sys.argv ha de ser de tres argumentos. el primero es el titulo
# del programa. 
if len(sys.argv) == 3:
# guardamos el texto enviado por consola. esta en la posicion 1 de la lista
# generada por sys.argv. 
	textoarepetir = sys.argv[1]

# vamos a repetir varias veces el texto transmitido por consola
# para ello primeramente capturamos numericamente el segundo argumento
# de la lista que sera un numero transmitido por consola. 
	repetir =int(sys.argv[2])

	for r in range(repetir):
		print(textoarepetir)
else:
	print("ERROR. Debe de introducir una cadena de texto,"+ 
		"\n y un numero que determine las repeticiones")

