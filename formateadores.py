#usos del metodo .format

print("Sammy tiene {} balones.".format(5)) 

open_string = "A Sammy le encanta {}." 
print(open_string.format("la lechona segoviana")) 

new_open_string = "A Sammy le gusta {} y {}." 
print(new_open_string.format("Jugar al Billar", "montar en bicicleta")) #Pass 2 strings into method, separated by a comma 

sammy_string = "Sammy loves {} {}, and has {} {}."
print(sammy_string.format("open-source", "software", 5, "balloons"))

print("Me gusta mas {0} que {1}!".format("vaguear", "trabajar")) 
print("Me gusta mas {1} que {0}!".format("vaguear", "trabajar")) 
# usando variables.
variable = "mentiroso"
print("el caballero, {0} {1} es un {pr}.".format("Jesus", "Cordoba", pr = variable))

# las iniciales de conversion son: s: STRING d: INTEGER f: FLOAT
print("Sammy comio {0:f} por ciento de una {1}!".format(75, "pizza")) 
# lo mismo pero CON LIMITANTES DE DECIMALES:
print("Sammy comio {0:.2f} por ciento de una {1}!".format(75, "pizza"))

# introduciendo espacios.
print("Sammy has {0:4} red {1:16}!".format(5, "balloons"))

#asi se alinea al centro con "^", de cincuenta caracteres. derecha > izquierda <
print("{:^100}".format("Estoy alineado en el centro de cien caracteres"))

print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))

# truncamiento de palabras
print("palabra cortada: "+"{:.4}".format("pasamontañas"))


# rellenos con caracteres, especificando los espacios
# la s es la inicial de conversion a: STRING
print("{:*^20s}".format("BIENVENIDOS"))

#combinacion espacios y recorte de decimales.
print("Sammy se come {0:5.0f} de la pizza".format(75.765367)) 

# con variables
sammy = "Sammy has {} balloons today!" 
nBalloons = 8 
print(sammy.format(nBalloons)) 

# numeros simples, cuadrados y cubos. 
for i in range(3,13): 
	print(i, i*i, i*i*i)

# ahora lo alineamos, con 3, 4, y 5 digitos: "d"
for i in range(3,13):

	print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))

# todos alineados a seis digitos. 
print("{:3} {:4} {:5}".format("enteros","cuadrados","cubos"))
for i in range(3,13): 
	print("{:6d} {:6d} {:6d}".format(i, i*i, i*i*i))

# rellenado: antes del numero de digitos introducir el caracter de relleno:
print("{:08d}".format(123))

# para alinear cifras, determinamos el numero de caracteres con sus decimales y puntos
# si los hubiere.
print("Alineando cifras: siete caracteres")
print("{:7.3f}".format(123.456000))
print("{:7.3f}".format(45.634))
print("{:7.3f}".format(2.3450000))
print("{:7.3f}".format(123))






