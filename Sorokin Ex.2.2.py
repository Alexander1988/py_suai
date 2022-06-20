# *Задание:* Придумайте целое двузначное число и "загадайте" его в коде программы.
# Пользователь вводит в консоль произвольное число. Если он угадал, программа выводит текст "да" и завершается.
# Если не угадал, программа выводит текст "нет" и дает еще одну попытку. Число попыток не ограничено.
#
# *Условия:* Используйте цикл while.
#
# *Пример:* (загадано число 33)
#
# [[Программа:]] Я загадала целое число, попробуйте угадать
# [[Пользователь:]] 11
# [[Программа:]] нет
# [[Пользователь:]] 22
# [[Программа:]] нет
# [[Пользователь:]] 33
# [[Программа:]] да
import random
n= None
py_program=random.randint(10,99)
print(py_program)

while py_program!=n:
    try:
        n=int(input('Hello! Guess what number am I thinking of? please, enter  an integer positive number: '))
    except:
        print("Invalid input. Pls. check the format of input data. ")
        continue
    if n==py_program:
        print("Whoa, you're right!! the number am I thinking of is " + str(n))
        break
    else:
        print("nope. I'm sorry, that's a  wrong number. Try again")






