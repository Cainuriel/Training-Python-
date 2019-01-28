class Coche():
	"""docstring for Coche"""
	def desplazamiento(self):
		print("Uso cuatro ruedas")

class Moto():
	def desplazamiento(self):
		print("Uso dos ruedas")

class Camion():
	"""docstring for Camion"""
	def desplazamiento(self):
		print("Uso seis ruedas")

# llama a cada metodo desplazamiento usando el polimorfismo. 
def comosemueve(objeto):
	objeto.desplazamiento()

#probemos el polimorfismo
clases = [Camion, Moto, Coche]
for i in clases:
	objeto = i()
	comosemueve(objeto)

