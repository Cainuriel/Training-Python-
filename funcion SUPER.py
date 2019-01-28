# ejemplo del uso de la funcion super

class Persona():
	def __init__(self, nombre, edad, residencia):
		self.nombre = nombre
		self.edad = edad
		self.residencia =  residencia

	def caracteristicas(self):
		print("Nombre: "+ str(self.nombre) + " Edad: " + str(self.edad) + " Residencia: " + str(self.residencia))

class Empleado(Persona):
# debemos introducir por parametro los valores del otro constructor heredado si queremos acceder a ellos
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

	#usamos la instruccion super para enviar estos valores al constructor de la superclase:
		super().__init__(nombre_empleado,edad_empleado, residencia_empleado)
		self.salario = salario
		self.antiguedad = antiguedad

#Sobre-escribimos el metodo e introducimos las nuevas variables de la subclase:
	def caracteristicas(self):
	#Usamos la instruccion super para incluir el metodo de la superclase:
		super().caracteristicas()

	#Ahora introducimos las nuevas caracteristicas en el metodo sobre-escrito:
		print("Salario: ",self.salario," Antiguedad: ",self.antiguedad, "anos")


antonio = Persona("Antonio Ramirez Cuesta",45,"Madrid")
antonio.caracteristicas()

paco = Empleado(34000, 5, "Francisco Marcos Estrada", 54, "Palma de mallorca")

paco.caracteristicas()

# funcion isinstance que devuelve True si el objeto es de la clase indicada. 
# se ha de introducir los dos parametros: objeto y clase:

#paco es persona, aunque se haya creado como Empleado. 
print(isinstance(paco,Persona))
# antonio, en cambio, no es Empleado
print(isinstance(antonio,Empleado))




		