import math
# recordar que las excepciones que creamos, detienen el programa.
def evaluarEdad(edad):
	if edad< 0:
		# tenemos que especificar un Error que exista. Salvo que creemos una clase como nuestro propio error. 
		raise TypeError("No se permiten edades negativas")
	if edad < 18:
		print("Eres menor de edad")
	elif edad < 45:
		print("Eres un adulto")
	elif edad < 65:
		print("Eres una persona madura")
	elif edad < 100:
		print("Eres un viejo, cuidate")

evaluarEdad(2)

def calcularRaiz(numero):

	if numero < 0:
		raise ValueError ("No se permiten numeros negativos")

	else:
		return math.sqrt(numero)

# podemos capturar nuestro propio error:
# de esa forma impedimos que se paralice el programa. 
op = (float(input("Deme un numero para realizar la raiz cuadrada: ")))

try:
	print(calcularRaiz(op))
except ValueError as Noqueremosnumerosnegativos:
	print(Noqueremosnumerosnegativos)


print("Fin del programa")
