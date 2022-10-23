### 8.1 Игра "Виселица"
#
# Программа "загадывает" слово и рисует в консоли такое количество подчёркиваний,
# сколько букв в слове.
# Пользователь начинает вводить буквы, чтобы отгадать слово.
# Если буква есть в слове, то программа обязана вписать её на своё место в слово
# (если таких букв несколько — то вписываются все), а
# если нет — то уменьшает число попыток на единицу (всего 10 попыток).
#
# Если отгадывающий не успел угадать слово раньше, чем истекло число попыток,
# то он считается проигравшим и должен угадывать следующее слово.
#
# Всё остальное - на Ваше усмотрение. Сдача будет проходить на вебинаре,
# поэтому загрузить программу в бот - можно (и нужно), но автотестов в для нее не будет.
#
# NB: при разночтениях с LMS версия задачи у бота - более точная.

import random

def get_random_word():
    WORDS = ("СТОЛОВАЯ", "РЕСТОРАН", "ШКОЛА", "СПРАВКА", "АНЕКДОТ", "ЗАВТРАК", "БИЗНЕС")
    word = random.choice(WORDS) #слово, которое нужно будет угадывать
    return word
#inputs
attempts = 10
position = None
new_word = get_random_word()
print(new_word)
letters_guessed = ["_"] * len(new_word)
# letters_guessed = ' '.join(letters_guessed)
lst_guesses = [] #letters which user entered
s = ""
#inputs

while  letters_guessed != list(new_word) and attempts > 0 :
    guess = input("Введите букву: \n").capitalize()
    if guess in new_word and guess not in lst_guesses:
        print("Молодец! буква угадана!")
        lst_guesses.append(guess)
        for index, letter in enumerate(new_word):
            if letter == guess:
                letters_guessed[index] = guess
        for letters in letters_guessed:
            print(letters, end=' ')

    else:

        if guess in lst_guesses:
            print("уже было")
            for letters in letters_guessed:
                print(letters, end=' ')
            print('')
            attempts = attempts - 1
        else:
            print("буква не угадана, попробуй ещё, товарищ")
            for letters in letters_guessed:
                print(letters, end=' ')

            attempts = attempts - 1
    if not "_" in letters_guessed:
        print('')
        print('Ураа! Победа!')
    else:
        if attempts == 0:
            print('теперь придется угадывать новое слово')
            attempts = 10
            position = None
            lst_guesses = []
            new_word = get_random_word()
            print(new_word)
        else:
            print('\n осталось:', attempts, 'попыток дружище')