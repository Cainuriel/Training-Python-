# aprenderemos que los tres puntos ... hacen la funcion de tabulacion de codigo
# util para la anidacion de pruebas en las que se usen condicionales o bucles. 
## ademas estos tres puntos se utilizan como comodines para atrapar excepciones. 
import math 

def listaraicescuadradas(Listanumeros):
	""" 
	la funcion devuelve una lista con la raiz cuadrada
	de los elementos pasados en otra lista por argumentos.

	>>> lista = []
	>>> for i in [4, 9, 16]:
	...		lista.append(i)
	>>> listaraicescuadradas(lista)
	[2.0, 3.0, 4.0]
	>>> lista = []
	>>> for i in [4, -9, 16]:
	...	lista.append(i)
	>>> listaraicescuadradas(lista)
	Traceback (most recent call last):
		...
	ValueError: math domain error


	"""

	return [math.sqrt(n) for n in Listanumeros ]

# print(listaraicescuadradas([4, 9, 16, 25, 36]))

import doctest

# recordamos que al ejecutar si todo va bien. NO DEBE DE DEVOLVER NADA. 
doctest.testmod()

