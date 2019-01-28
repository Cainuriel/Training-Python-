email = ""
veces = 0

def pediremail():
	email = input("introduzca un e-mail correcto, por favor: ")
	veces = email.count('@')

def numerodearrobas():
	while veces == 0:
		print("No tiene arroba")
		pediremail()

	while  veces > 1:
		print("mucha arroba por aqui, vuelva a empezar")
		pediremail()

	

def posicionarroba():
	length = len(email)
	posicion = email.find('@')

	if posicion == 0:
		print("No puede colocar la arroba al principio")
		pediremail()

	if posicion == length-1:
		print("La arroba esta al final. incorrecto")
		pediremail()

	print("Su email es valido. Muchas gracias")

pediremail()
numerodearrobas()
posicionarroba()


