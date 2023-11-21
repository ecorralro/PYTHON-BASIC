### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado" # imprime \n con la doble barra
print(my_scape_string)

# Formateo

name, surname, age = "Eugenio", "Corral", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #introduce el valor de las variables con el .format
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) #introduce el valor de las variables de cada tipo
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #es la forma más dummie
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #necesita la f inicial para formatear las variables

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3] #muestra contenido entre esas posiciones
print(language_slice)

language_slice = language[1:] # muestra desde esa posición hasta el final
print(language_slice)

language_slice = language[-2] # muestra la posición contando desde el final
print(language_slice)

language_slice = language[0:6:2] # son los caracteres que no se van a mostrar
print(language_slice)

# Reverse

reversed_language = language[::-1] # lo muestra del revés, desde el final se empieza desde la posición -1 y no 0
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize()) # primera en mayuscula
print(language.upper()) # todas en mayuscula
print(language.count("t")) # contar algo
print(language.isnumeric()) # es un número?
print("1".isnumeric())
print(language.lower()) # todas minusculas
print(language.lower().isupper())
print(language.startswith("Py")) # booleano de empieza por?
print("Py" == "py")  # No es lo mismo