# Lista de listas
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz)

# Mostrar cada elemento de la lista almacenada en la fila 0
print(matriz[0][0], '=> fila: 0, columna:0')
print(matriz[0][1], '=> fila: 0, columna:1')
print(matriz[0][2], '=> fila: 0, columna:2')

# Iterar matriz
for element in matriz:
    print(element)

print('*' * 20)

# Iterar listas dentro la lista

for row in matriz:       # Itera cada fila en la matriz
    print(row)
    for column in row:   # Itera cada columna de cada fila
        print(column)

for row in matriz:       # Itera cada fila en la matriz
    print(row, '<= fila',matriz.index(row))
    for column in row:   # Itera cada columna de cada fila
        print(column, '<= columna', row.index(column))

for row in matriz:       # Itera cada fila en la matriz
    print(row, '<= fila',matriz.index(row))
    for column in row:   # Itera cada columna de cada fila
        print(column, '<= [', matriz.index(row), '][', row.index(column), ']')



