class Vehiculo():
# Los constructores en Python poseen todos el mismo nombre que es el siguiente:
	def __init__(self):
# la encapsulacion de variables se realiza con los dos guiones bajos "__" delante de la variable:
		self.__ruedas = 4
		self.__peso = 1000
		self.__enmarcha = False
	color = "Blanco"

	def arrancar(self, encender):
		self.__enmarcha = encender

# llamada del metodo encapsulado. 

		if self.__enmarcha:
			chequeo = self.__chequear()

		if self.__enmarcha and chequeo:
			return	print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRrrrmmmmmmmmmmmm.....")
			
		elif self.__enmarcha and chequeo==False:
			print("Atencion: Problemas detectados, no podemos arrancar el coche")


		else:
			return print("El coche esta parado")

	def caracteristicas(self):
		print("El color del coche es: " + str(self.color) + " y ademas tiene " + str(self.__ruedas) + " ruedas.")

# para encapsular metodos y que no sean accesibles desde fuera de la clase, usar igualmente los dos guiones: "__"
	def __chequear(self):
		niveles = "ok"
		puertas = "cerradas"
		if niveles == "ok" and puertas == "cerradas":
			print("Todo Ok...")
			return True
		else:
			return False

		
seat = Vehiculo()
print("Creamos el coche seat")
seat.arrancar(True)
seat.caracteristicas()




print("Ahora vamos a crear otro objeto, ford:")
# manipulamos las caracteristicas de este segundo objeto de forma bien simple.
ford = Vehiculo()
ford.arrancar(False)
ford.color = "Rojo"




ford.caracteristicas()

print("Tienen el mismo color los dos coches?")
if ford.color == seat.color:
	print("Tiene el mismo color que es: " + str(seat.color))
else:
	print("No. el color del seat es " + str(seat.color)+" y el color del ford es "+str(ford.color))
