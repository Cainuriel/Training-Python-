# las funciones decoradoras son funciones que embeben a otras. Es decir, es una funcion que
#envuelve a otra. Es una forma de introducir codigo repetido en muchas funciones.

def funcion_decoradora_BBDDs(Funcion_a_decorar):

	# IMPORTANTE. toda funcion decoradora tiene una funcion interna.
	# ella tiene que ser devuelta con un return, y es la encargada de
	# envolver a la funcion exterior. 
	def funcion_interna():
		print("Conectando con bases de datos..")

		Funcion_a_decorar()

		print("Cerrando base de datos.")

	# NO OLVIDAR DEVOLVER LA FUNCION INTERNA
	return funcion_interna


# para decorar la funcion se escribe encima de la funcion parasitada
# con una arroba.

@funcion_decoradora_BBDDs
def funcion_exterior():
	i = 0
	respuesta = input("escriba los datos de busqueda: ")

	print("Procesando datos")

	while (i < 5):
		print("..bib...bib...bib...")
		print("procesando...")
		i += 1
	respuesta = input("Aqui los tiene. Desea algo mas? ")
	print("Hasta la proxima")
	



funcion_exterior()


# lo mismo con parametros.
def dando_parametros(funcion_exterior):

	# el asterisco indica que no sabemos el numero de parametros que se introduciran. Es indefinido.
	# los dos asteriscos, son para keyword arguments, es decir, argumentos con valores por defecto.
	def funcion_interna(*args, **kwargs):
		print("Ahora realizaremos una suma o una resta")

		#no olvidarse colocar el asterisco. 
		funcion_exterior(*args, **kwargs)

		print("hemos finalizado las operaciones de la funcion")
	return funcion_interna

@dando_parametros
def suma(a, b, c):
	c = (a + b + c)
	print(c) 

@dando_parametros
def resta(a,b):
	c = (a - b)
	print(c)


@dando_parametros
def potencia(clavevalor=5, clavevalor2=3):
	print(pow(clavevalor,clavevalor2))


suma(12,34,2)
resta(90,23)
#en esta llamada calculara los valores por defecto.
potencia()
potencia(23,2)


