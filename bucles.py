# estructura del bucle for, variable, y el elemento a recorrer que puede ser: tupla, string, o rango..
elemento_a_recorrer=[1,2,3,4]

for variable in elemento_a_recorrer:

	print("Hola mundo")
# la variable contador, serian los elementos que compongan la estructura, sea esta del tipo que sea:
elemento_a_recorrer2 = ["una", "dos", "tres"]
for variable in elemento_a_recorrer2:
	print("Hola mundo recorrido con strings")

# para imprimir los elementos de un array o tupla bastaria con imprimir la variable que recorre el elemento:

for variable in elemento_a_recorrer2:
	print(variable)

# se pueden usar los caracteres de un string para recorrer un bucle directamente:

for variable in "recorre mi cuerpo":
	print("XZ")

# bucle con range

for i in range(5):
	print(i)

#ejercicio de imprimir numeros impares, uno detras del otro.
modulo = 0
for i in range(100):
	modulo= i % 2
	if modulo != 0:
		print(i,end=" ")

# ejercicio para determinar si una contrasena es correcta:

password = input("Introduzca password. Recuerde que ha de ser mayor de ocho caracteres y no disponga de espacios: ") 
error = 0
contador = 0
for i in password:
	contador=contador + 1
	if i == " ":
		error = 1
if error > 0 or contador < 8:
	print("password incorrecto")
else:
	print("password correcto")



# y por ello, de forma facil se pueden hacer comprobaciones de caracteres de un string
# comprobemos con un ejercicio que evalua una cuenta de correo.

contador = 0
email = False
entrada = input("introduzca su email: ")
for i in entrada:
	if i=="@":
		contador=contador + 1
		for i in entrada:
			if i==".":
				email=True
		
		

if email and contador==1:
	print("email correcto, continue.")
else:
	print("email incorrecto, fuera.")






	