# Tuples

# CRUD Create, Read, Update & Delete
# Create
numbers = (1,2,3,5)
print(numbers)
print(type(numbers))

strings = ('nico', 'zule', 'santi')
print(strings)
print(type(strings))

# Read
print(numbers)
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])

# Update, Delete -> Al ser inmutables, no permiten modificar elementos
# print(numbers)
# numbers[1] = 'change'

print('**Otros métodos','*' * 10)
# Otros métodos
# - index -> devuelve la posición en la que esta el elemento indicado
print(strings)
print(strings.index('zule'))

print('*' * 10)
# - count -> cuenta cuantas veces está un elemento dentro de la tupla
print(strings)
print(strings.count('nico'))

print('*' * 10)
# Transformar tupla en lista
my_list = list(strings)
print(my_list)
print(type(my_list))

print('*' * 10)
# - Agregar elementos
print(my_list)
my_list[1] = 'juli'
print(my_list)

print('*' * 10)
# Transformar lista en tupla
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)