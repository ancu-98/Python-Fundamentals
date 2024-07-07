# Ciclo for

'''
Función range()

for element in range(20):
    print(element)

for element1 in range(1,21):
    print(element1)

'''

# Iterar Lista
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

# Iterar tupla
my_tuple = ('sebas', 'juli', 'santi')
for element in my_tuple:
    print(element)

print('*' * 20)

# Iterar diccionario
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

# Cuando iteramos con for un diccionario,
# nos itera sobre las keys, y con ellas podemos acceder al valor

# Iterar keys
for key in product:
    print(key)

print('*' * 20)

# Iterar values
for value in product:
    print(product[value])

for value in product.values():
    print(value)

print('*' * 20)

# Iterar pares key-value
for key in product:
    print(key, '=>', product[key])

for key, value in product.items():
    print(key, '=>', value)

print('*' * 20)

# Iterar lista de diccionarios
people = [
    {
        'name': 'sebas',
        'age': 34
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 23
    },
    {
        'name': 'cami',
        'age': 26
    }
]

# Iterar diccionario almacenado en cada posición de la lista
for person in people:
    print(person)

# Iterar los valores con keys iguales a 'name' de cada diccionario
for person in people:
    print('name =>',person['name'])