milista=["maria", "carla", "marta","antonio"]
# para imprimir una lista entera:
print(milista[:])
#impresion de un elemento de la lista:
print(milista[3])
# con numeros negativos cuenta desde el final:
print(milista[-3])
print(milista[-2])
print(milista[-1])
# se pueden imprimir porciones de lista, colocando el rango entre dos puntos, y siendo el segundo numero excluido:
print(milista[0:2])
print(milista[2:3])
# si no se coloca el primer numero del rango, Python entiende que es el cero:
print(milista[:2])
# Y si se coloca el primer numero del rango, entonces entiende que es hasta el final:
print(milista[1:])
# añadir nuevos elementos a la lista:
milista.append("Sandra")
print(milista[:])
# para insertar elementos en una posicion en concreto se usa la funcion insert:
milista.insert(2,"Luis")
print(milista[:])
# se pueden concatenar listas facilmente con la funcion "extend":
milista2=["Enrique","Cristina","Fernando"]
milista.extend(milista2)
print(milista[:])
#funcion index para imprimir el indice de un elemento:
print(milista.index("Enrique"))
#Si buscamos el indice de un elemento que esté repetido nos dará el indice del primero:
milista2.append("maria")
print(milista.index("maria"))
print(milista[:])
# funcion booleana "in" para saber si se encuentra un elemento en una lista:
print("maria" in milista)
print("antonio" in milista2)
# funcion "remove" para borrar elementos en una lista
milista.remove("Fernando")
#para eliminar el ultimo elemento de una lista funcion "pop"
milista.pop()
# el operador suma puede concatenar listas tambien como la funcion "extend":
milista3=milista2+milista

# incluso se pueden multiplicar

milista4=["uno",1,1.1] * 5
print(milista4[:])