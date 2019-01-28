# vamos a capturar errores: errores de valor, y de division por cero.

# el bucle infinito nos sirve para asegurarnos de que se introduzca correctamente los valores. 
#se sale de el, cuando se han introducido correctamente. 
def dividir():
	while True:
		try:
			num1 =int(input("primer numero, dividendo: "))
			num2 =int(input("segundo numero, divisor: "))
			break
		except ValueError:
			input("introduzca valores númericos por favor")
		
	resultado = 0
	try:
		resultado = num1/num2
	except ZeroDivisionError:
		print("No se puede dividir por cero")
		dividir()


	print("El resultado de la division de: "+ str(num1)+ " entre "+ str(num2) +" es: "+ str(resultado))
	print("El programa, continua ejecutandose")


dividir()
