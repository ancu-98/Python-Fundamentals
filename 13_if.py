# if
if True:
    print('Debería ejecutarse')

if False:
    print('Nunca se ejecutará')

# else
stock = input('Ingrese el número de stock => ')
stock = int(stock)

if stock >= 100 and stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')

# elif

# - Ejemplo 1
pet = input('¿Cuál es tu mascota favorita? ')

if pet == 'perro':
    print('genial')
elif pet == 'gato':
    print('genial tienes buen gusto')
elif pet == 'pez':
    print('eres lo máximo')
else:
    print('no tienes ninguna mascota')
    print('o tienes otro tipo de mascota')


# - Ejemplo 2
x = 10

if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")

# - Ejemplo 3
number = input('Digita un número => ')
number = int(number)

module = number % 2

if module == 0:
  print('Es par')
else:
  print('Es impar')