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

while True:
    try:
        n=int(input('please, enter integer number in a range of 0 to 1000 '))
    except:
        print("Invalid input. Pls. check the format of input data. ")
        continue
    numbers=list()
    divider=7
    for number in range(n+1):
        if number%divider==0 and number!=0:
            numbers.append(number)
    if numbers !=[]:
        print(f'  these numbers are multiples of 7: {numbers}')



