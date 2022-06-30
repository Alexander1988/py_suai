# *Задание:* Пользователь вводит в консоль целые числа по одному.
# Когда пользователь вводит пустую строку, программа выводит
# наибольшее четное число из ранее введенных и завершает работу.
#
# *Условие* Не использовать контейнерные типы данных, такие как списки и кортежи
#
# *Пример:*
# ```
# [Программа:] Вводите целые числа по одному, для окончания введите пустую строку:
# [Пользователь:] 1
# [Пользователь:] 7
# [Пользователь:] 2
# [Пользователь:] -1
# [Пользователь:]
# [Программа:] 2
# ```
largest = None

#start the finite loop
while True:
    num = input("Вводите целые числа по одному, для окончания введите пустую строку: ")
    if num == "" :
        break
    #check the weakest place in code
    try:
        n = int(num)
    except:
        #if input invlaid inform user
        print("Invalid input")
        #go to the start of the loop
        continue

        #find the largest number
    if largest is None:
        largest = n
    elif n>largest:
        largest = n
#printout the largest and the smallest
print(largest)


