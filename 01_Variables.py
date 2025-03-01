# Variables

my_variable = "My String variable"
print(my_variable)

my_int = 5
print(my_int)

my_int_to_str_variable = str(my_int)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool = True
print(my_bool)

# Concatenación de variables en un print
print(my_variable, my_int_to_str_variable, my_bool)
print("Este es el valor de:", my_bool)
# Algunas Funciones de sistema
print(len(my_variable))#cuenta los caracteres de la variable

# Variables en una sola línea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs

name = input('What is your name: ')
age = input('How old are u? ')

print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
