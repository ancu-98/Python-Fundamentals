# CRUD Create, Read, Update & Delete
print('**CRUD','*' * 10)
# Create
numbers = [1,2,3,4,5]
# Read
print(numbers[1])
# Update
numbers[-1] = 10
print(numbers)
# Delete
del numbers[-1]
print(numbers)

print('**Agregar elementos','*' * 10)

# Agregar elementos

# - Agregar elementos al final de una lista
numbers.append(700)
print(numbers)

print('*' * 10)

# - Insertar elemento en un índice
numbers.insert(0, 'Hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

print('*' * 10)

# - Combinar listas

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(numbers)
print(tasks)
print(new_list)

print('**Eliminar elementos','*' * 10)

# Eliminar elementos

# - remove -> elimina el elemento que indicamos
print(new_list)
new_list.remove('todo 1')
print(new_list)

print('*' * 10)

# - pop -> Elimina el último elemento
print(new_list)
new_list.pop()
print(new_list)
# o elimina el elemento en el indice especificado
new_list.pop(0)
print(new_list)

print('**Otros métodos','*' * 10)

# Otros métodos

# - index -> devuelve la posición en la que esta el elemento indicado
print(new_list)
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

print('*' * 10)

# - reverse -> invierte el orden de la lista
print(new_list)
new_list.reverse()
print(new_list)

print('*' * 10)

# - sort() -> Ordena listas
# Listas de números
numbers_a = [1,4,6,3]
print(numbers_a)
numbers_a.sort()
print(numbers_a)

# Listas de strings
strings = ['re', 'ab', 'ed']
print(strings)
strings.sort()
print(strings)

# Pero no ordena listas mixtas
# print(new_list)
# print(new_list.sort())