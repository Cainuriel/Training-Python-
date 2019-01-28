print("ordenar en una lista diccionario los entrenadores y los pokemons con esta estrctura")
print("entrenador: tal... pokemon: pascual...")

lista = [["ash", "nodian"],
		["ash", "charmander"],
		["Misty", "Picachu"],
		["Misty", "Squirtle"]]

lista_diccionario = []

# la tupla engancha la lista dentro de la lista.
for tupla in lista:
	lista_diccionario.append({"Entrenador":tupla[0],
								"Pokemon":tupla[1]})

print(lista_diccionario)

# otra forma es des-empaquetando:
lista_desempaquetando = []
for entrenador, pokemon in lista:
	lista_desempaquetando.append({"Entrenador":entrenador,
								"Pokemon":pokemon})
# mas visual en mi entender

print("metodo des-empaquetando")
print(lista_desempaquetando)

print("Segundo ejercicio:")
print("Hacer una funcion que devuelva las cinco letras mas comunes de una frase")

from collections import Counter

frase = "Vamos a ver si es capaz de deducir cuales son las cinco letras mas comunes de esta frase \n"

def contar_letras(frase):
	# comprension de lista con un for y el condicional que substrae la puntuacion irrelevante
	contador = Counter(letra for letra in frase if letra not in " .,\n")
	# parametro: numero de elementos mas comunes.
	return contador.most_common(5)

print(contar_letras(frase))

print(""" Ejerccio tres: Crear una funcion que nos devuelva el coeficiente de Jaccard de dos lista
	de elementos. Este coeficiente de Jaccard es una medida de similaridad entre dos grupos:
	Se define Numero de elementos de los dos frupos / entre el numero de elementos de cada grupo""" )

lista1 = [1,2,3,4,5]
lista2 = [1,6,7,8,9]

print("tendremos que primeramente las listas transformarlas en conjuntos con la funcion set")

def jaccard(lista1, lista2):
	conjunto1 = set(lista1)
	conjunto2 = set(lista2)
	print("unimos los conjuntos en uno")
	union = len(conjunto1.union(conjunto2)) # nos interesa el numero de elementos, no el conjunto en si. 
	print(union)
	print("Y despues realizamos la interseccion")
	interseccion = len(conjunto1.intersection(conjunto2)) # nos interesa el numero de elementos, no el conjunto en si. 
	print(interseccion)
	jaccard = interseccion / union
	print("El coeficiente de Jaccard es: {:.2f}".format(jaccard))

jaccard(lista1,lista2)

