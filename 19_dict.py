# Create
my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': 'bla bla bla',
    'name': 'Sebastian',
    'last_name': 'Bernal',
    'age': 98
}

print(my_dict)
print(len(my_dict))

print('*' * 20)

# Read
print(my_dict['age'])
print(my_dict['last_name'])
'''
get -> Devuelve el valor para una clave especificada.
Si la clave no existe, devuelve None o un valor predeterminado.
Ayuda a verificar si una clave existe o no.
'''
print(my_dict.get('age'))

# in
print('avion' in my_dict)
print('otroqueno' in my_dict)