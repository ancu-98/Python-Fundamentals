# indexing
text = 'Ella sabe Python'
print(text)
print('index 0 =>',text[0])
print('index 1 =>',text[1])

# Obtener el último caracter de una cadena
# - forma 1
size = len(text)
print('size =>', size)
print(text[size - 1])

# - forma 2
print(text[-1])

# slicing
print(text)
print(text[0:5])
print(text[10:16])
# desde el inicio hasta el indice 10
print(text[:10])
# desde el indice 5 hasta el final
print(text[5:])
# desde el inicio hasta el final
print(text[:])
print('*' * 10)
# slicing con salto
print(text)
# desde el indice 10 hasta el indice 16 con 1 salto
print(text[10:16:1])
# desde el indice 10 hasta el indice 16 con 2 saltos
print(text[10:16:2])
# desde el inicio hasta el final con 2 saltos
print(text[::2])