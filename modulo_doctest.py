
# probamos las pruebas de test en la documentacion.


def areatriangulo(base, altura):
    """
    Realiza el calculo del area de un triangulo.

    >>> areatriangulo(3,6)
    9.0

    >>> areatriangulo(2,2)
    2.0
    """
    return base * altura / 2

def tienearroba(email):
	"""
	Comprueba si tiene una arroba
	tambien da error si tiene mas de una.
	argumento: email
	>>> tienearroba('amor@gmail.com')
	'El email es correcto'
	>>> tienearroba('amor@@gmail.com')
	'El email no es correcto'
	>>> tienearroba('amorgmail.com')
	'El email no es correcto'
	>>> tienearroba('amorgmail.com@')
	'El email no es correcto'
	
	"""
	arroba = email.count('@')
	if (arroba != 1 or email.rfind('@') == len(email)-1):
		return 'El email no es correcto'
		
	else:
		return 'El email es correcto'
		


# en este modulo se pueden ejecutar las pruebas que existan dentro de la documentacion.
# estas pruebas se preparan despues de tres > y se ha de colocar el resultado que
# deberia otorgar la prueba.

# solo devuelve algo si hay error.
if __name__ == "__main__":
    import doctest
    doctest.testmod()










