import random

options = ('piedra', 'papel', 'tijera')

user_wins = 0
computer_wins = 0
rounds = 1

while True:

    print('*' * 20)
    print(' ' * 5, 'ROUND', rounds)
    print('*' * 20)

    print(' ' ,'computer_wins =', computer_wins)
    print(' ' ,'user_wins =', user_wins)
    print('*' * 20)

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('esa opción no es valida')
        continue

    computer_option = random.choice(options)

    print('User_option =>', user_option)
    print('Computer_option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('User ganó!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('Computer ganó!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'tijera':
            print('tijera gana a papel')
            print('Computer ganó!')
            computer_wins += 1
        else:
            print('papel gana a piedra')
            print('User ganó!')
            user_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('User ganó!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Computer ganó!')
            computer_wins += 1

    if computer_wins == 2:
        print('El ganador es la computadora')
        break

    if user_wins == 2:
        print('El ganador es el usuario')
        break
    rounds += 1
