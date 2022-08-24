# ### 6.3 Подсчет цифр
#
# Задание: Пользователь вводит в консоль целое положительное число,
# от 0 до 2 миллиардов.
# Программа считает, сколько раз во введенном числе встречается каждая из
# 10 арабских цифр и выводит количество повторов каждой цифры, как в примере ниже,
# и завершает работу.
# Вывод количества повторов осуществляется в порядке увеличения цифр, от 0 до 9.
# Если какая-то из цифр не встретилась, для нее выводится 0.
#
# Примечание: Обязательно использование словаря (dict).
#
# Пример:
# [Программа:] Введите число
# [Пользователь:] 123123123
# [Программа:]
# 0: 0
# 1: 2
# 2: 2
# 3: 2
# 4: 0
# 5: 0
# 6: 0
# 7: 0
# 8: 0
# 9: 0
#
#
#
# NB: при разночтениях с LMS версия задачи у бота - более точная.

num = input('Введите число\n')
res={}

for digit in num:
    for arab_digit in range(0,10):
        if digit == arab_digit:
            res[digit] = num.count(digit)
        else:
            res[arab_digit] = num.count(str(arab_digit))
#print(res)
for k,v in res.items():
    print(f'{k}: {v}')



