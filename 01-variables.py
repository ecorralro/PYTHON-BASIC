# VARIABLES

# En Python no se usa CamelCase, su buena práctica es snake_case
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

# Conversión de tipo => str(string)
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. !OJO! Se puede pero no es buena práctica
name, surname, alias, age = "Eugenio", "Corral", 'Uge', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Eugenio"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección" # Dejamos claro que queremos q sea un string, pero posteriormente se puede forzar, es un tipado débil
address = True
address = 5
address = 1.2
print(type(address))