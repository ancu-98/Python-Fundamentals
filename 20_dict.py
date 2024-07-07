person = {
    'name' : 'Sebas',
    'last_name': 'Bernal',
    'langs': ['python', 'javascript'],
    'age': 98
}

print(person)

# Update
person['name'] = 'Santi'
# restar 50 a la edad actual
person['age'] -= 50
# agregar otro valor-value a una clave-key
person['langs'].append('java')
print(person)

# Delete
# Eliminar pares key-value
del person ['last_name']
# pop -> Sin argumento, eliminar el último elemento.
# Pero en diccionarios debemos enviar la clave como argumento para eliminar el par.
person.pop('age')
print(person)

# Métodos útiles
# items -> Devuelve una vista de los pares clave-valor del diccionario.
# devuelve una lista(o array) en pares key-value de tuplas.
print('Items')
print(person.items())

# keys -> Devuelve una vista de las claves del diccionario.
# devuelve una lista(o array) con cada clave
print('Keys')
print(person.keys())

# values -> Devuelve una vista de los valores del diccionario.
# devuelve una lista(o array) con cada valor
print('Values')
print(person.values())