# los generadores devuelven de forma iterable, uno a uno, cada secuencia de valores 
# u objetos que genere. A diferencia de una funcion que genere una secuencia, 
# que la devuelve completa en su creacion. 
# forma clasica de generar un generador. a traves de una funcion:
# funcion que genera numeros pares. se transmite un limite de numeros por parametro.
def generarpares (limite):
	num = 1
	milista = []

	while num<limite:
		milista.append(num*2)
		num +=1
	return milista

print(generarpares(10))

# ahora realizamos el mismo programa con un generador.

def generadorpares(limite):
	num =1
	while num<limite:
		yield num*2
		num +=1
# creamos una variable que guarde el objeto iterado

par = generadorpares(10)

# para imprimirlos todos, podemos usar un bucle:
#for i in par:
#	print(i)

# pero con la instruccion next nos devuelve el primer valor del generador:

print(next(par))

print("aqui ejecutariamos otro codigo y despues llamamos otra vez al generador")

print(next(par))
print(next(par))

print("tantas veces como lo necesitamos devolviendo los valores uno a uno")
print(next(par))
print(next(par))
print(next(par))
print(" controlando la produccion de los objetos generados")






