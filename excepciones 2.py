# capturando excepciones de forma consecutiva

def division():
	try:
		num1 =float(input("primer numero, dividendo: "))
		num2 =float(input("segundo numero, divisor: "))
		print("El resultado es: " + str(num1/num2))
	except ZeroDivisionError:
		print("Division entre cero no valida")

	except ValueError:
		print("introduzca numeros, no otro tipo de caracteres")
	

	print("Gracias por utilizar nuestro programa")

division()

# para atrapar todas las excepciones de un programa basta con NO ESPECIFICARLAS:

def dividir():
	try:
		num1 =float(input("primer numero, a dividir: "))
		num2 =float(input("segundo numero, que divide: "))
		print("El resultado es: " + str(num1/num2))
		# no especificamos la excepcion y capturamos todas.
	except:
		input("Ha ocurrido un error, y no se ejecutara la operacion")
	
	# la clausula finally garantiza la ejecucion de un codigo, se de error o no.
	#indispensable para cerrar conexiones con BBDD si ocurre un error, por ejemplo.
	finally:
		print("Gracias por utilizar nuestro programa")

dividir()