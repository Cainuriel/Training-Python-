# tuplas son listas fijas. no alterables. mas optimas si no tenemos pensado alterar los valores de sus elementos.
mitupla=(1, 2, 3, 4)
print(mitupla[3])
#para crear listas de tuplas se usa el metodo "list":
milista=list(mitupla)
# para convertir listas a tuplas el metodo "tuple"
mitupla=tuple(milista)
# la impresion de una tupla se diferencia de una lista en la que aparece entre parentesis.

# el metodo "count" nos dice cuantas veces se encuentra un elemento en una tupla
mitupla2=(1,1,2,2,1,1,1,1,1,1,1,1,1,1,1)
print(mitupla2.count(1))
# metodo "len" para saber cuantos elementos tiene una tupla
print(len(mitupla2))

# se pueden crear tuplas unitarias, colocando un unico elemento seguido de una coma:

mituplaunitaria=("solito estoy",)
print(mituplaunitaria)
print(len(mituplaunitaria))

# Se pueden crear tuplas sin colocar los parentesis aunque no se recomienda. se llama EMPAQUETADO DE TUPLA:
tuplasinparentesis="dos",2,2.2
print(tuplasinparentesis)

#el DESEMPAQUETADO DE TUPLAS es sacar los elementos de una de ellas a varias variables y se hace de esta forma:
letras, numero1, numero2 = tuplasinparentesis
print(letras, numero1, numero2)