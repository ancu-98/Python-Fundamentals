name = 'Sebastian'
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))

print('Sebastian' + ' Bernal')
print(10 + 20)
print('Sebastian' + '98')

# Conversión de entero <--> string
# Ejemplo de entero a string
age = 98
print('Mi edad es ' + str(age))
print(f'Mi edad es {age}')

# Ejemplo de string a entero
age = input('Escribe tu edad => ')
print(type(age))
age = int(age)
age += 10
print(f'en 10 años tu edad será: {age}')