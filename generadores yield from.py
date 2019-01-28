# cuando colocamos un asterisco en un argumento o parametro estamos indicando 
#que no sabemos el numero de elementos que se recibiran, y que ademas, 
# que vendran en una tupla.creamos el generador

def dameCiudades (*ciudades):
	for i in ciudades:
		yield i
# y ahora, la variable-objeto que recogera los elementos, en este caso ciudades.
recogedor = dameCiudades("Madrid", "Barcelona", "Sevilla", "Zaragoza", 
	"Bilbao", "Cartagena", "Santiago de Compostela", "Cordoba", "Granada", "Valencia")
# imprimimos las dos primeras ciudades
print(next(recogedor))
print(next(recogedor))
# ahora lo creamos con un bucle anidado para entrar en los sub-elementos
# de los elementos de la tupla; en este caso: las letras de las ciudades.
def dameletraciudad (*ciudades):
	for i in ciudades:
		for j in i:
			yield j
recogedor2  = dameletraciudad("Madrid", "Barcelona", "Sevilla", "Zaragoza", 
	"Bilbao", "Cartagena", "Santiago de Compostela", "Cordoba", "Granada", "Valencia")
print(next(recogedor2))
print(next(recogedor2))
# pues bien, el uso del yield from nos ahorra el segundo bucle
# su syntax seria de la siguiente forma:
def dameletraciudadconyieldfrom(*ciudades):
	for i in ciudades:
		yield from i
recogedor3 = dameletraciudadconyieldfrom("Madrid", "Barcelona", "Sevilla", "Zaragoza", 
	"Bilbao", "Cartagena", "Santiago de Compostela", "Cordoba", "Granada", "Valencia")
print(next(recogedor3))
print(next(recogedor3))

# ejemplo: con comprension de listas. 
# ATENCION. Comprueba como faltan dos letras, que son las dos iteraciones anteriores.
print([letrasciudades for letrasciudades in dameletraciudad(recogedor2)])

#Nos quedamos en Barcelona, vayamos a la siguientes ciudades.
print(next(recogedor))
print(next(recogedor))

# CONSEJO: INTENTA CAPTURAR EL FIN DE LA ITERACION SI DESCONOCES CUANDO SERA. 
# YA QUE TE DARA ERROR.

