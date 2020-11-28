print("Think about number and i will guess it in 10 moves ..")


def guessing_number():
    min_ = 0
    max_ = 1000
    guessing = True
    while guessing:
        guess = int((max_ - min_) / 2) + min_
        print(f'Zgaduję: {guess}')
        answear = input("Tell your information to computer [too much, too small, you guessed ")
        if answear == 'you guessed':
            guessing = False
            print('I win !!')
        elif answear == 'too much':
            max_ = guess
        elif answear == 'to small':
            min_ = guess
        else:
            print("Don't cheat!")


guessing_number()
