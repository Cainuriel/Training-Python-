# funcion iter()

# vamos a convertir listas y cadenas en algo iterable.

lista = [1,2,3,4,5,6,7,8,9]
cadena = "Deletreame por favor"
listaiterada = iter(lista)
cadenaiterada = iter(cadena)

print("primera iteracion")
print(next(listaiterada))
print(next(cadenaiterada))
print("segunda, tercera y cuarta iteracion")
print(next(listaiterada))
print(next(cadenaiterada))
print(next(listaiterada))
print(next(cadenaiterada))
print(next(listaiterada))
print(next(cadenaiterada))



