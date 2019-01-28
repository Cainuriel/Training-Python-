print("Condicional con elseif")

edad_usuario=int(input("Introduzca edad: "))

if edad_usuario<18:
	print("No puede pasar")
# el famoso else if de otros lenguajes se escribe en python:
elif edad_usuario>100:
	print("Edad incorrecta")
else:
	print("Adelante...")