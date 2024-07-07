name = 'Sebastian'
last_name = 'Bernal Cuesta'
print(name)
print(last_name)

# Concatenar Strings
full_name = name + ' ' + last_name
print(full_name)

quote = "I'm Sebas"
print(quote)

quote2 = 'She said "Hello"'

# format
template = ' Hola, mi nombre es ' + name +' y mi apellido es ' + last_name
print('V1' + template)

template = ' Hola, mi nombre es {} y mi apellido es {}'.format(name,last_name)
print('V2' + template)

template = f' Hola, mi nombre es {name} y mi apellido es {last_name}'
print('V3' + template)