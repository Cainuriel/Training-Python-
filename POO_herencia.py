class Vehiculos():

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

# la herencia se realiza introduciendo la superclase dentro de los parentesis de la clase

class Furgonetas(Vehiculos):
	pesoextra = 0
	def cargar(self,carga):
		self.pesoextra = carga

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

		if self.pesoextra == 0:
			print("Vehiculo sin carga")
		else:
			print("El vehiculo lleva una carga de "+ str(self.pesoextra) + " kilos.")

		

class Motos(Vehiculos):
	
	hacercaballito = ""

	def caballito(self):
		self.arrancar()
		self.acelerar()

		self.hacercaballito ="Rueda delantera levantada: " + "Mira, mira, mira lo que hago!!"


#SOBRE-ESCRITURA DE METODOS: Simplemente copiamos el metodo de la superclase, y cambiamos lo que se considere.
	def estado(self):
			print("Marca: "+ self.marca + "\nModelo: " + self.modelo + "\n" + self.hacercaballito)

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



moto = Motos("Honda", "VGR")

moto.caballito()
moto.estado()

print("-------------------------")
furgo = Furgonetas("Ford", "Transit")

# cargamos la furgo con un par de kilos
furgo.cargar(20)

furgo.estado()

class Electricos():
	# has tenido que inicalizar la variable fuera del constructor para que te funcionase.
	carga = False

	def __init__(self):
		self.carga = True 

	def estadobateria(self):
		return self.carga
	
	def cargarbateria(self,enchufar):
		if enchufar:
			self.carga = True



#HERENCIA MULTIPLE: Simplemente, introduciendo las superclases como parametros en la subclase
# ATENCION MUY IMPORTANTE: SE DA PREFERENCIA AL CONSTRUCTOR DE LA PRIMERA CLASE, NO A LAS SUBSIGUIENTES;

class BicicletasElectricas(Motos,Electricos):

	


	def estado(self):
		print("Marca: "+ self.marca + "\nModelo: " + self.modelo + "\n" + self.hacercaballito)

		if self.enmarcha:
			print("El Vehiculo esta en marcha")
			self.carga = False
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

		if self.estadobateria():
			print("Bateria Llena")

		else:
			print("Bateria baja. Debe enchufar la Bicicleta")

	




mibicielectrica = BicicletasElectricas("Mountain","ElectricBike")

print("-------------------------")


mibicielectrica.estado()

print("-------------------------")

mibicielectrica.cargarbateria(True)

mibicielectrica.estado()



print("-------------------------")

mibicielectrica.caballito()

mibicielectrica.estado()

print("-------------------------")





