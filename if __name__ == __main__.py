
def hacer_algo():
	""" si el programa es importado, entonces solo ejecutará
 			el print de la funcion hacer_algo """
	print("algo")
	    

    

if __name__ == "__main__":
	print('Ejecutando como programa principal')
	hacer_algo()


# sacando los comentarios. 
print(hacer_algo.__doc__)
print(help(hacer_algo))



