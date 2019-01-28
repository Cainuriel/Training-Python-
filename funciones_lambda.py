import math
# las funciones lambda pretenden simplificar el codigo
# son funciones anonimas que no pueden utilizar bucles y condicionales. 

# calculo de triangulo de forma tradicional.
"""def areatriangulo(base, altura):
	return (base * altura) / 2


print(areatriangulo(5,7))"""

# calculo con lambda
# los dos puntos funcionan como si fuese un "return"
areatriangulo = lambda base, altura:(base * altura) / 2

print(areatriangulo(5,7))

al_cubo = lambda numero: numero**3
al_cubo2 = lambda numero: pow(numero, 3)

print(al_cubo(13))
print(al_cubo2(13))

# formato con funciones lambda
# colocas interrogantes porque no encontraste las exclamaciones.. :)
destacar_valor = lambda comision: "¿{}? $".format(comision)

ana = 2345

print(destacar_valor(ana))

f = lambda x, y : x + y

print("resultado: ",f(2 , 2))

a = lambda x : math.factorial(x)
print("Factorial de 5: ",a(5))



