# la instruccion continue ignora vueltas del bucle
# vamos a imprimir letras de un texto, ignorando el guion que las separa:

for letra in "Guarda-ropa":
	if letra=="-":
		continue
	print("letras del texto sin el guion: "+ letra)


#la instruccion pass devuelve un null en un bucle. 
# poca utilidad. dejar una implementacion de una clase, bloques de codigo, ecta, para mas tarde.

class miclase:
	pass # se implementara mas tarde.

#el extrano uso del else en un bucle. puede llevarnos a confusion al verlo.
# en el siguiente ejemplo lee el codigo del else si el bucle termina, sino, es saltado por la instruccion break.

email = input("deme su correo: ")

for i in email:
	if i=="@":
		arroba = True
		break
else:
	arroba = False
print(arroba)
