# probando la funcion superior filter.
# El operador filter(f, l) necesita una función f como primer argumento. 
#f devuelve un valor booleano, es decir, verdadero o falso. 
#Esta función se aplicará a cada elemento de la lista. 
#Solo si f devuelve True, el elemento de la lista se incluirá en la lista de resultados.

def numerospares(numero):
	if numero % 2==0:
		return True

listadenumeros = [3,2,34,11,13,17,19,2]

# acemos UN CASTING para que nos devuelva el resultado en forma de lista.
# los PARAMETROS de la funcion "FILTER" son: 1` metodo, 2` elementos.
print(list(filter(numerospares,listadenumeros)))

#practicamos el uso de funcion lambda

print(list(filter(lambda numero: numero%2==0,listadenumeros)))


# uso de filter con objetos.
class Empleado():
	def __init__(self, nombre, cargo, salario):

		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario

	# metodo que imprime la informacion determinada para cuando se intente imprimir al objeto.
	def __str__(self):
		return "{} trabaja como {} y cobra: {}".format(self.nombre, self.cargo, self.salario)


listaempleados = [
Empleado("Fernando","Informatico", 25000),
Empleado("Juan","Informatico", 45000),
Empleado("Maria","Limpiadora", 19000),
Empleado("Antonio","Administrativo", 23000),
Empleado("Sara","Analista", 43000),
]

salariosmasgrandesque25000 = filter(lambda empleado: empleado.salario > 25000,listaempleados)

for i in salariosmasgrandesque25000:
	print(i)

