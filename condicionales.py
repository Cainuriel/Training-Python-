print("condicional sencillo")
# IMPORTANTE para python todo lo que entra a traves de la funcion INPUT es texto.

damelanota=input("Introduzca nota: ")

def evaluacion(nota):
# es necesario cambiar su valor a entero para realizar el condicional. en este caso la funcion "int"

	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(int(damelanota)))

