# Ciclo while

'''
Evitar ciclo infinito
while True:
    print('se ejecuto')
'''
counter = 0

# El ciclo se ejecuta mientras counter sea menor que 10
while counter < 10:
    counter += 1
    print(counter)

print('*' * 20)

counter1 = 0

# Control del ciclo

# break -> termina el ciclo inmediatamente, independientemente de la condición.
# El ciclo se ejecuta mientras counter sea menor que 10
while counter1 < 20:
    counter1 += 1
    if counter1 == 15:     # Si counter es igual a 15
        break             # Se detiene la ejecución
    print(counter1)

print('*' * 20)

counter2 = 0

# continue -> omite el resto del bloque de código en la iteración actual
# y pasa a la siguiente iteración del ciclo.
while counter2 < 20:
    counter2 += 1
    if counter2 < 15:     # Si counter es igual a 15
        continue          # Pasa a la siguiente iteración
    print(counter2)       # omitiendo las líneas siguientes