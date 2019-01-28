
ejemplo = "Ejemplo"
# convierte en mayusculas upper() y en minusculas lower():

print(ejemplo.upper())
ejemplo = "HOLA"
print(ejemplo.lower())

# capitalize(), convierte la primera letra en mayuscula 
ejemplo = "antonio"
print(ejemplo.capitalize())

# count(), cuenta las veces que aparece una cadena o una letra en un texto
ejemplo = "Adivina cuantas veces aparece en este texto la letra 'a'"
print(ejemplo.count('a'))

ejemplo = "busca lo repetido busca lo repetido cuantas veces sale lo repetido"
print(ejemplo.count("lo repetido"))

# find() da la posicion o indice de una letra o grupo de caracteres
print("la palabra: veces, esta en la posicion: ",ejemplo.find("busca"))

# isdigit() nos dice si es una cifra o no lo es. devuelve un booleano. 

numero = "123"
letras = "jejejejeje"
letrasynumeros = "12amigos"
print("numero escrito en letras: ", numero.isdigit())
print("letras sin numeros: ",letras.isdigit())
print("letras con numeros: ",letrasynumeros.isdigit())


# isalnum() comprueba si es alfanumerico.
signos = "/?>?"
print(signos.isalnum())
print(letras.isalnum())

# isalpha() comprueba si solo hay letras los espacios no cuentan.

ejemplo = "Que pasa amigo"

print("Si tiene espacios dara falso ",ejemplo.isalpha())
print("Si no los tiene, dara true ",letras.isalpha())


# split() separa por palabras utilizando los espacios como separadores

ejemplo = "En un lugar de la mancha"
print(ejemplo.split())
# separamos dos palabras, el resto quedaran juntas
print(ejemplo.split(None,2))
# cortamos por donde indiquemos
print(ejemplo.split("lugar"))

# strip() borra espacios sobrantes al principio y al final

ejemplo = "           jejejeje      "
print(ejemplo.strip())

# replace() cambia una palabra o letra por otra dentro de un string
ejemplo = "Eres un poco tonto"

print(ejemplo.replace("un poco tonto", "muy listo"))


# rfind() devuelve la ultima posicion de la cadena. si no encuentra devuelve -1

ejemplo = "buscaremos el 1 pero a partir de aqui. ya vereis que saldra este: 1"
print("buscamos el ultimo uno: ", ejemplo.rfind("1"))



