# not
print(not True)
print(not False)

# and
print('NOT AND')
print('True and True => ', not (True and True))
print('True and False => ', not (True and False))
print('False and True => ', not (False and True))
print('False and False => ', not (False and False))

stock = input('Ingrese el número de stock => ')
stock = int(stock)

print(not(stock >= 100 and stock <= 1000))


# or
print('NOT 0R')
print('True or True => ', not (True or True))
print('True or False => ', not (True or False))
print('False or True => ', not (False or True))
print('False or False => ', not (False or False))

role = input('Digita el rol => ')

print(not(role == 'admin' or role == 'seller'))