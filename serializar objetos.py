import pickle
class Vehiculo():

# IMPORTANTE Si cargas archivos binarios de objetos en archivos en donde NO esten las clases de los mismos
# obtendras un error. 

	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True
# el salto de linea se realiza con la barra hacia la izquierda y la letra n "\n"
	def estado(self):
		print("Marca: "+ self.marca + "\nModelo: " + self.modelo )

		if self.enmarcha:
			print("El Vehiculo esta en marcha")
		else:
			print("El Vehiculo esta detenido")

		if self.acelera:
			print("El Vehiculo esta acelerando")
		else:
			print("El Vehiculo no esta acelerando")

		if self.frena:
			print("El Vehiculo esta frenando")
		else:
			print("El Vehiculo no esta frenando")

coche1 = Vehiculo("Ford","Escort")
coche2 = Vehiculo("Fiat","500")
coche3 = Vehiculo("Seat","Ibiza")

coches = [coche1,coche2,coche3]

# creamos el archivo donde guaradaremos los coches

Vehiculos = open("Vehiculos","wb") # recordamos el modo de escritura binaria wb...

pickle.dump(coches,Vehiculos)

Vehiculos.close()

del (coches)

# rescate del fichero que hemos creado:

fichero_apertura = open("Vehiculos","rb")

miscoches = pickle.load(fichero_apertura)

fichero_apertura.close()

for c in miscoches:
	print(c.estado())

