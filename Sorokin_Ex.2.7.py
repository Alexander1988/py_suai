# *Задание:* Придумайте целое трехзначное число и "загадайте" его в коде программы.
# Пользователь вводит в консоль произвольное число. Если он угадал, программа выводит текст "да" и завершается.
# Если не угадал, программа выводит текст "больше", если загаданное число больше введенного,
# или "меньше", если загаданное число меньше введенного, и дает еще одну попытку. Максимальное число попыток - 10.
# Если за 10 попыток пользователь не угадал, выводится сообщение "не угадали"
#
# *Условия:* Используйте цикл while.
#
# *Пример:* (загадано число 333)
#
# [[Программа:]] Я загадала целое число, попробуйте угадать
# [[Пользователь:]] 11
# [[Программа:]] больше
# [[Пользователь:]] 100
# [[Программа:]] больше
# [[Пользователь:]] 800
# [[Программа:]] меньше
# [[Пользователь:]] 333
# [[Программа:]] да


import random
n= None
attempt=0 #total attempts number is 10.
py_program=random.randint(10,99)
print(py_program)

while attempt<=10:
    attempt+=1
    try:
        n=int(input('Hello! Guess what number am I thinking of? please, enter  an integer positive number: '))
    except:
        print("Invalid input. Pls. check the format of input data. ")
        continue
    if n==py_program:
        print("Whoa, you're right!! the number am I thinking of is " + str(n))
        break
    elif n>py_program:
        print("that's number bigger than guessed number")
    elif n<py_program:
        print("that's number smaller than guessed number")
    elif attempt==10:
        print("I'm sorry, You've made a 10 tries. Number is not guessed")