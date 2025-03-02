### Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [21, 24, 31, 43, 53, 31, 23, 42]

print(len(my_list))

my_other_list = [35, 1.77, "hola", "comoestas"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("hola"))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

print(list([1,2,3,4]))

my_other_list.append("Moure")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_list = "hola python"

print(my_list)
print(type(my_list))