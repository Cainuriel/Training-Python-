class Persona():
	def __init__(self, nombre, edad, Lugar_residencia):
		self.nombre=nombre

		self.edad=edad

		self.Lugar_residencia=Lugar_residencia

	def descripcion(self):
		print("Nombre: ", self.nombre, " Edad: ", self.edad, "Lugar de Residencia: ", self.Lugar_residencia)

class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, Lugar_residencia_empleado):


		# llamamos al constructor de la superclase y le introducimos los datos correspondientes asi:
		super().__init__(nombre_empleado, edad_empleado, Lugar_residencia_empleado)

		self.salario = salario

		self.antiguedad = antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ", str(self.salario), " Antiguedad: ", str(self.antiguedad))


Antonio=Persona("Antonio", 55, "España")

Antonio.descripcion()

Ricardo = Empleado(1500, 15, "Ricardo", 43, "Mexico")
Ricardo.descripcion()
# La instruccion isinstance es igual a instanceof de Java. devuelve true si el objeto es de la clase, 
# y false si no lo es.
# la clase a comparar se introduce como segundo parametro:

print(isinstance(Ricardo,Empleado))
print(isinstance(Antonio,Empleado))



