# para crear un paquete en la carpeta tiene que haber un archivo con el nombre:
__init__.py

# el archivo se creara vacio.

# para llamar a los modulos dentro de un paquete se escribe asi:

from nombre_paquete.nombre_modulo import nombre_funcion # o usar el asterisco.

# se puede crear sub carpetas dentro de carpetas, o paquetes dentro de paquetes para ordenar
# mejor el codigo. para ello no hay que olvidar colocar en cada una de estos sub paquetes
# el archivo vacio con el nombre:
__init__.py

# para instalar paquetes primeramente creamos un archivo setup.py en el que se describe el
# informacion variada.
# en este archivo se escribe lo siguiente:

from setuptools import setup

setup(
	
 	name = "nombre del paquete",
 	version = "0.0",
 	description = "Descripcion breve de lo que hace el paquete",
 	author = "Nombre del autor",
 	author_email = "email del autor",
 	url = "direccion de la url del autor o empresa",
 	packages = ["carpeta_principal","carpeta_principal.subcarpetas_que_existiesen"]

	)
# despues se llega a el a traves de la consola del sistema.

# o abrir el PowerSell apretando la tecla shift y despues el boton derecho en la carpeta donde 
#reside el archivo. en este caso seria en la carpeta Python. 

# a continuacion en la consola, se escribe lo siguiente pare crear un paquete distribuible:
# ATENCION SON INSTRUCCIONES DE CONSOLA NO LENGUAJE PYTHON:

python setup.py sdist

# esto creara dos carpetas una acabada en ".egg-info", mas otra llamada "dist"
# de distribucion donde habra un archivo comprimido.

#Instalar un paquete en el ordenador

#de nuevo, a traves de consola escribir la siguiente instruccion:
pip3 install "nombredelpaquete"

# para desinstalar el paquete del python del sistema operativo simplemente escribir en consola:
pip2 uninstall "nombredelpaquete"