import math

# el tipo range es muy versatil en el uso de rangos numericos. algunos ejemplos:
# de un numero a un numero, el primero inclusive:
for i in range(5,10):
	print(f"valor de la variable: {i}")
#introduciendo un tercer numero, determinamos la distancia de rango en el conteo:
# por ejemplo, para ir de dos en dos, desde el numero 50 al 70 lo definimos asi:
for i in range(50,71,2):
	print(f"valor de la variable: {i}")

# bucles con while

i=1
while i<=10:
	#otra forma de concatenar texto con variables
	print("valor de la variable: "+ str(i))
	i = i + 1
print("Fin de la impresion")

print("Programa que calcula la raiz cuadrada")
numero=int(input("Introduce un numero: "))
intentos = 0

while numero< 0:
	if intentos==2:
		print("Te estas pitorreando de mi. cerramos el programa")
		break
	print("Numero negativo no operable. por favor, introduce uno correcto")
	numero=int(input("aqui: "))
	intentos = intentos + 1
if (intentos<2):
	resultado = math.sqrt(numero)
	print("La raiz cuadrada de "+str(numero)+" es:"+str(resultado))



