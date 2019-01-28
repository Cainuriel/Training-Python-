
# Coincidencia de cumpleaños entre cincuenta personas.
prob = 1.0
asistentes = 50

for i in range(asistentes):
	# dias del año.
    prob = prob * (365-i)/365

print("Probabilidad de que compartan una misma fecha de cumpleaños es {0:.2f}"
      .format(1 - prob))



# calculamos los subconjuntos posibles.
monedas = [5,5,5, 10,10,10, 20,20,20, 50,50,50, 1,1,1, 2,2,2]
def potencia(c):
    """Calcula y devuelve los subconjuntos del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]



prob = 1.0
bolsillos = 600

conjuntos = potencia(monedas)
print("numero de conjuntos ",len(conjuntos))
numero_conjuntos = len(conjuntos)

for i in range(bolsillos):
	# numero de conjuntos: 64
    prob = prob * (numero_conjuntos-i)/numero_conjuntos

print("Probabilidad de que compartan una mismo conjunto de monedas {0:.2f}".format(1 - prob))


