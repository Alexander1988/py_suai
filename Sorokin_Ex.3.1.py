# *Задание:* Пользователь вводит в консоль целое число от 0 до 1000.
# Необходимо напечатать все числа, кратные 7, не превышающие заданное число.
# Если таких чисел нет, программа не должна ничего выводить.
# *Условия:* Используйте цикл for.
#
# *Пример:*
# ```
# [Программа:] Введите число:
# [Пользователь:] 35
# [Программа:] 7
# [Программа:] 14
# [Программа:] 21
# [Программа:] 28
# [Программа:] 35
# ```


n=int(input('Введите число: \n'))
print("Invalid input. Pls. check the format of input data. ")
divider=7
for number in range(n+1):
    if number%divider==0 and number!=0 and number <= 1000:
        print(number)




