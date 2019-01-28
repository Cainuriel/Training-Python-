class Numeros():
	def __init__(self, uno, dos, tres, cuatro):
		self.uno = uno
		self.dos = dos
		self.tres = tres
		self.cuatro = cuatro

	def imprimir(self):
		print(self.uno, self.dos, self.tres, self.cuatro)

ejemplo = Numeros(1,2,3,8)
ejemplo.imprimir()
