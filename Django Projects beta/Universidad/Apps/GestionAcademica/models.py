from django.db import models

class Alumno(models.Model):
    apellido = models.CharField(max_length= 38)
    apellido2 = models.CharField(max_length= 38)
    Nombre = models.CharField(max_length= 38)
    DNI = models.CharField(max_length= 9)
    Nacimiento = models.DateField
    sexos = (('M','Masculino'),('F','Femenino'))
    sexo = models.CharField(max_length= 1, choices= sexos)

    def datosAlumno(self):
        cadena = "{0},{1}{2}{3}"
        return cadena.format(self.DNI,self.Nombre,self.apellido,self.apellido2)


    def __str__(self):
        return self.datosAlumno()

class Curso(models.Model):
    Nombre = models.CharField(max_length= 50)
    Creditos = models.PositiveSmallIntegerField(default= 25)
    Estado = models.BooleanField(default= True)

    def __str__(self):
        return "{0}, Creditos: {1}".format(self.Nombre,self.Creditos)

class Matricula(models.Model):
    Alumno = models.ForeignKey(Alumno,null= False, blank= False, on_delete= models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        cadena = "Alumno: {0}, Matriculado en {1}"
        return cadena.format(self.Alumno, self.Curso.Nombre)


