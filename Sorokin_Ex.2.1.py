# 2.1 Все чётные
#
# *Задание:* Пользователь вводит в консоль целое положительное число. Необходимо вывести все четные положительные числа, меньшие заданного числа.
#
# *Условия:* Используйте цикл while. Выводите каждое число с новой строки.
#
# *Пример:*
#
# [[Программа:]] Введите целое положительное число
# [[Пользователь:]] 11
# [[Программа:]]
# 2
# 4
# 6
# 8
# 10
while True:
    try:
        n=int(input('please, enter  an integer positive number: '))
    except:
        print("Invalid input. Pls. check the format of input data. ")
        continue
    while n>0:
        n=n-1 #since the output positive numbers should be smaller than n, we should decrease n.
        if n%2==0 and n>0:
            print(n)
            n=n-1
