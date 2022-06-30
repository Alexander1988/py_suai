# *Задание:* Пользователь вводит в консоль целое число от 0 до 1000.
# Необходимо напечатать в порядке убывания все числа, кратные 7, не превышающие заданное число.
# Если таких чисел нет, программа не должна ничего выводить.
#
# *Условия:* Используйте цикл for. Не используйте условный оператор.
#
# *Примечание:* функция `range`, которую часто используют c циклом for,
# имеет три аргумента (начальное значение, конечное значение и шаг) и
# позволяет формировать возрастающие и убывающие последовательности с произвольным шагом.
#
# *Пример:*
# ```
# [Программа:] Введите число:
# [Пользователь:] 29
# [Программа:] 28
# [Программа:] 21
# [Программа:] 14
# [Программа:] 7
# ```

while True:
    try:
        n=int(input('please, enter integer number in a range of 0 to 1000 '))
    except:
        print("Invalid input. Pls. check the format of input data. ")
        continue
    rem=None
    divider=7
    res=set() #creating of empty set()

    for number in range(n,0,-1):
        rem=number%divider
        number-=rem #since, this actio creates same number we need set()
        res.add(number)

    res.pop()#removes '0'
    b=list(res)#sort function is not supported by sets
    b.sort(reverse=True)
    # print(res)
    for i in b:
        print(i)


    #     if number%divider==0:
    #         numbers.append(number)
    # if numbers !=[]:
    #     print(f'  these numbers are multiples of 7: {numbers}')