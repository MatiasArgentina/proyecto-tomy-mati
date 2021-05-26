#Solo Crear una clase
class Person:
    pass
#Agregar una Instancia
jorge =  Person()
#Agregar una Instancia
jorge =  Person()
#Agregar Atributos a la Clase
class Person:
    name = ''
    school = ''
#A las instancias les podemos agregar atributos, pero a las ya creadas no
#se le actualizan los atributos aunque actualizemos la clase.
jorge.name = 'Jorge'
jorge.school #Jorge se creo antes de agregar el atributo

#Ana que se creo despues si tiene ambos atributos.
ana = Person()
ana.name
ana.school
ana.name = 'Ana'
ana.school = 'Universidad de la vida'

#Ahora agregamos metodos, self tiene que estar en la definicion del metodo y es el objeto en si.
class Person:
    name = ''
    school = ''
    
    def print_name(self):
        print(self.name)

    def print_school(self):
        print(self.school)

romi = Person()
romi.name = "Romina"
romi.print_name()

# Metodos con parametros
class Person:
    name = ''
    school = ''
     
    def print_information(self, name, school):
        print(self.name)
        print(self.school)
             
esteban = Person()
esteban.name = 'Esteban'
esteban.school = 'Universidad Esteban'
esteban.print_information(esteban.name, esteban.school)
esteban.print_information(22, 33) #No esta usando los parametros.

# Si definimos parametros el iniciar la clase
class Person:
    def __init__(self, n, s):
        self.name = n
        self.school = s
     
    def print_name(self):
        print(self.name)
         
    def print_school(self):
        print(self.school)
     
rober = Person('Roberto', 'Universidad Rober de la vida')
 
rober.print_name()
rober.print_school()