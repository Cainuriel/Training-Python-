import pickle 

# creamos un fichero que pueda leer el archivo binario. utilizamos el modo "rb"
fichero = open("Nombres","rb")

#utilizamos el metodo "load" para cargar la informacion:

nombres = pickle.load(fichero)
fichero.close()

for i in nombres:
	print(i)
