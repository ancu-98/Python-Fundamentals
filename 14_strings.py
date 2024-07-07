# Operador in
text = 'Ella sabe programar en Python'
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print('Elegiste Python, excelente decisión!!')
else:
    print('Considera aprenderlo!!')

# Método len
text1 = 'Ella sabe programar en JavaScript'
size = len(text1)
print(size)

# Método upper y lower
print(text1)
print(text1.upper())
print(text1.lower())

# Método count
print(text1)
print(text1.count('a'))

# Método swapcase
print(text1)
print(text1.swapcase())

# Método startswith y endswith
print(text1)
print(text1.startswith('Ella'))
print(text1.endswith('Python'))

# Método replace
print(text1)
print(text1.replace('JavaScript', 'Rust'))

# Métodos capitalize y title
text2 = 'este es un título'
print(text2)
print(text2.capitalize())
print(text2.title())

# Método isdigit()
print('321'.isdigit())