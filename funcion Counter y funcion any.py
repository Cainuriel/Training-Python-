# si se repite tres veces un numero en la primera parte, y dos veces
#en la segunda. devolver 1. Si no es asi, devolver cero.
# el metodo Counter crea un Diccionario con la cuenta de caracteres.
from collections import Counter

num1 = 10560002
num2 = 100
def triple_double(num1, num2):
	double = Counter(str(num2))
	triple = Counter(str(num1))
	print(double),print(triple)
	for i in range(10):
		if triple[str(i)] >= 3:
			for j in range(10):
				if double[str(j)] >= 2:
					return 1
					break
	return 0

def triple_double2(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])

print(triple_double(num1, num2))
print(triple_double2(num1, num2))

# create a temporary list
my_list = []

# go through digits 0-9
for i in '0123456789':

    # check if this digit appears 3 times in 'num1' and 2 times in 'num2'
    # and append the result to my_list
    my_list.append( i*3 in str(num1) and i*2 in str(num2) )

# return 'True' if any of the checks were true, otherwise 'False'
print("con la funcion any: ",any(my_list))
