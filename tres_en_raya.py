# clase que genera turnos.
from collections import deque

turno = deque(["X","O"])
tablero = 	[["","",""],
			["","",""],
			["","",""]]

def cambiarturno():
	turno.rotate()
	return turno[0]

def imprimirtablero(x, y):
	tablero[x][y] = cambiarturno()
	print(tablero[0])
	print(tablero[1])
	print(tablero[2])

def jugadorhumano():
	posicion = []
	j = 0
	coo =str(input("Digite las coordenadas: "))
	for i in coo:
	 if i not in " ,":
	 	posicion.append(i)
	 	j+= 1
	try:
		imprimirtablero(int(posicion[0]),int(posicion[1]))
		isfinal(tablero)
	except:
		input("Escriba bien. Aprete enter para continuar")
		jugadorhumano()

	

def isfinal(tablero):
	for x in tablero:
		for y in x:
			if y == "":
				jugadorhumano()
	print("Empate amigo")


jugadorhumano()




