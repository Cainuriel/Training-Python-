# biblioteca pickle para la serializacion
import pickle 

lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]

# creamos el fichero en donde guardaremos la informacion
# en el modo deberemos especificar que es escritura binaria con el argumento "wb"

fichero_binario = open("Nombres","wb")

#utilizamos el metodo para volcar datos de la bibilioteca pickle:
# DOS PARAMETROS: la informacion a volcar, y el fichero externo en el que se archivara.
pickle.dump(lista_nombres,fichero_binario)
fichero_binario.close()
# se puede borrar el fichero de la memoria con el metodo "del"
del(fichero_binario)

