    #* Tuples 

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (34,1.77,"obed", "perez") 
print(my_tuple) #? (34, 1.77, 'obed', 'perez')
print(type(my_tuple)) #?  <class 'tuple'>

print(my_tuple[0]) #? 34
print(my_tuple[-1]) #? perez
# print(my_tuple[4]) #!IndexError
# print(my_tuple[-6]) #!IndexError 

print(my_tuple.count("perez")) #? 1 
print(my_tuple.index("perez")) #? 3

my_other_tuple = (13,34,24)

#my_tuple[1] = 1.90 #!IndexError 
# TODO: esto sucede debido a que las tuplas son variables obligatoriamente constantes e inmutable

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) #? (34, 1.77, 'obed', 'perez', 13, 34, 24)

print(my_sum_tuple[3:6]) #? ('perez', 13, 34)

my_tuple = list(my_tuple)
print(type(my_tuple)) #? <class 'list'>

my_tuple.insert(4, "roberto")
my_tuple.insert(1, "azul")
print(my_tuple) #? [34, 'azul', 1.77, 'obed', 'perez', 'roberto']

my_tuple = tuple(my_tuple)
print(type(my_tuple)) #? <class 'tuple'>

#del my_tuple[2] #! TypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) #! NameError: name 'my_tuple' is not defined
