# aplica funciones a cada elemento de una lista o tupla iterable...
# la diferencia con la funcion "filter" 
# es que ésta ultima, solo devuelve en base a una condicion booleana. 

class Empleado():
	def __init__(self, nombre, cargo, salario):

		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	# metodo que imprime la informacion determinada para cuando se intente imprimir al objeto.
	def __str__(self):
		return "{} trabaja como {} y cobra: {}".format(self.nombre, self.cargo, self.salario)


listaempleados = [
Empleado("Fernando","Informatico", 1200),
Empleado("Juan","Informatico", 1560),
Empleado("Maria","Limpiadora", 980),
Empleado("Antonio","Administrativo", 1100),
Empleado("Sara","Analista", 3100),
]

def comision(empleado):

	# incrementamos el salario un 3%
	empleado.salario = empleado.salario * 1.03

	return empleado

# 1` parametro: funcion. 2` parametro: lista o tupla a operar. 
# el resultado es una lista.
aumentodesueldo = map(comision,listaempleados)

# mostramos resultados:
for e in aumentodesueldo:
	print(e)




