# Creación lista y acceso a elementos
numbers = [1,2,3,4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])

# Modificar elementos - mutar

'''
Los strings no son mutables
text = 'Hola'
text[0] = 'W'
'''
print(tasks)
tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

# Seleccionar elementos de una lista

# Desde el inicio hasta el indice 3
print(numbers)
print(numbers[:3])

# Operador in
print(types)
print(True in types)
print('hola' in types)