### Classes ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        #self.full_car = brand + color
        #self.full_car = f"{brand} {color}"
my_car=Car("Audi", "Rojo")
print(my_car.brand,my_car.color)

class Person:
    def __init__(self, name, surname, alias="Sin alias"): # Constructor
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name # Forma de acceder a una propiedad privada, == getter

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Eugenio", "Corral")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Eugenio", "Corral", "Uge")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Cristina Grau"
print(my_other_person.full_name)

my_other_person.full_name = 1234
print(my_other_person.full_name)