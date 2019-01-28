import pickle

class persona():
	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado a una persona. Se llama: ", self.nombre)

# metodo que crea una cadena de texto con la informacion de un objeto:

	def __str__(self):
		return "{}{}{}".format(self.nombre, self.genero, self.edad)


# IMPORTANTE: CADA VEZ QUE EJECUTES ESTE PROGRAMA GUARDARA EN UN ARCHIVO EXTERNO
# EL OBJETO QUE AQUI CREES. PRUEBA A CAMBIAR LAS CARACTERISTICAS DEL OBJETO PERSONA
# Y EJECUTA EL PROGRAMA. COMPROBARAS COMO SE GUARDA PERMANENTE EN EL ARCHIVO.
persona1 = persona("Antonio ","Hombre ",51)


class listapersonas():
	personas = []

	# el constructor genera el archivo permanente en donde almacenaremos a las personas
	# el modo "ab+" permite agregar de forma binaria
	def __init__(self):
		fichero_personas = open("Ficheros Personas","ab+")
	# colocamos el cursor al principio para poder leer a todas las personas
		fichero_personas.seek(0)

		try:
			self.personas = pickle.load(fichero_personas) # cargamos datos en la lista
			print("Se cargaron {} personas del fichero externo".format(len(self.personas))) # indicamos numero de personas
		except:
			print("Fichero vacio") # mensaje de error en el caso de que el fichero este vacio
		finally:
			fichero_personas.close()
			del (fichero_personas) # siempre ejecutaremos estas dos instrucciones, independientemente de la excepcion.

	def agregarPersonas(self, p):
		# metodo "append" para agregar a la lista objetos
		self.personas.append(p)
		self.guardarpersonasenficheroexterno()

# este metodo parece igual al de mostrarinfodeficheroexterno... ????
	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarpersonasenficheroexterno(self):
		fichero_personas = open("Ficheros Personas","wb")
		pickle.dump(self.personas,fichero_personas)
		fichero_personas.close()
		del (fichero_personas)

	def mostrarinfodeficheroexterno(self):
		print("Informacion del fichero externo: ")
		for p in self.personas:
			print(p)

# creamos un objeto que agregue a las personas a una lista:

lista_personas = listapersonas()

lista_personas.agregarPersonas(persona1)

lista_personas.mostrarinfodeficheroexterno()


