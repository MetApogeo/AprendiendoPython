    #* Sets

my_set = set()
my_other_set = {}

print(type(my_set)) #? <class 'set'>
print(type(my_other_set)) #? <class 'dict'> 
#TODO:Inicialmente es un diccionario si lo declaramos con {}

my_other_set = {"obed", "perez", 21}
print(type(my_other_set)) #? <class 'set'>

print(len(my_other_set)) #? 3

#print(my_other_set[0]) #! TypeError: 'set' object is not subscriptable

my_other_set.add("Met")
print(my_other_set) #? {'Met', 'obed', 21, 'perez'}
#* Un set no es una estructura ordenada

my_other_set.add("Met")
print(my_other_set) #? {'Met', 'obed', 21, 'perez'}
#* Un set NO admite datos repetidos

print("obed" in my_other_set) #? True
print("oved" in my_other_set) #? False

my_other_set.remove("obed")
print(my_other_set) #? {'perez', 21, 'Met'}

my_other_set.clear()
print(my_other_set) #? set()
print(len(my_other_set)) #? 0

del my_other_set
#print(my_other_set) #! NameError: name 'my_other_set' is not defined

my_set = {"obed", "perez", 21}
my_list = list(my_set)
print(my_list) #? ['perez', 'obed', 21]
print(my_list[0]) #? perez

my_other_set = {"roberto", "carlos", 32}

my_new_set = my_set.union(my_other_set)
print(my_new_set) #? {32, 'roberto', 21, 'carlos', 'obed', 'perez'}
print(my_new_set.union(my_new_set)) #? {32, 'roberto', 21, 'carlos', 'obed', 'perez'}
print(my_new_set.union(my_new_set).union({"JavaScript", "Python", "C#"})) 
#? {32, 'C#', 'obed', 'JavaScript', 'Python', 21, 'carlos', 'roberto', 'perez'}

print(my_new_set.difference(my_set)) #? {32, 'carlos', 'roberto'}