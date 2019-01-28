# los diccionarios se crean con llaves, y la clave:valor con dos puntos:

midiccionario = {"Alemania":"Berlin","Francia":"Paris","Italia":"Roma"}

#Acceso por clave. La clave siempre es el primer termino, y el valor el segundo:
print(midiccionario["Italia"])

#se agrega de la siguiente forma:
midiccionario["Rusia"]="moscu"
# para eliminar elementos de un diccionario:
del midiccionario["Rusia"]

print(midiccionario)

# uso de tuplas con diccionarios:

mitupla=(1,2,3,4,5)
diccionarionumerosescritos={mitupla[0]:"Uno",mitupla[1]:"Dos",mitupla[2]:"Tres"}
print(diccionarionumerosescritos)
# Se puede guardar tuplas en diccionarios
diccionariocontupla={"Hola":"Adios","Decada de los ochenta":[1980,1981,1982,1983,1984,1985,"ecta"]}
print(diccionariocontupla["Decada de los ochenta"])

# usando llaves en vez de corchetes, podemos hacer diccionarios de diccionarios...
diccinariodediccionarios={"Hola":"Mundo","Superheroes":{"Klark":"Superman","Peter":"Spiderman"}}
print(diccinariodediccionarios["Superheroes"])
#metodo "keys" para visualizar las claves de un diccionario:
print(midiccionario.keys())
# los valores se imprimen con el metodo "values"
print(midiccionario.values())
# funcion "len" para conocer el tamano:
print(len(midiccionario))


