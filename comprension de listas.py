# podemos comprimir una lista de muchas formas
# con un bucle
deletrear = [palabra for palabra in "Supercaliflastilistico"]
print(deletrear)

#potencias de 2 de los primeros veinte numeros
cuadrados = [numero**2 for numero in range(1,20)]
print(cuadrados)

# comprension de listas con condicional
# saber si un numero es par.

espar = [par for par in range (2,101) if par%2 == 0]
print(espar)

# finalmente una comprension de lista dentro de una comprension
# con un condicional. sacaremos los pares de las potencias de dos.

espardepotencias = [par2 for par2 in [par2**2 for par2 in range(1,20)] if par2%2 == 0]
print(espardepotencias)
