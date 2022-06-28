# *Задание:* Число-"нарцисс" в десятеричной системе счисления - это такое число, которое равно сумме своих цифр, возведенных в степень, равную количеству его цифр.
# Например, таким число является 351 = 3**3 + 5**3 + 1**3
#
# Пользователь вводит целое число в диапазоне 0 до 999.
# Программа выводит в консоль слово *нарцисс*, если введенное число удовлетворяет вышеописанному условию. В противном случае
# программа выводит произвольный текст.
#
# *Примечание:* Для разложения числа на десятеричные разряды воспользуйтесь примером кода, который был рассмотрен на лекции.
#
# *Пример 1:* (ввод нарциссического числа)
#
# [[Программа:]] Введите целое число
# [[Пользователь:]] 153
# [[Программа:]] нарцисс
#
# *Пример 2:* (ввод другого числа)
#
# [[Программа:]] Введите целое число
# [[Пользователь:]] 517
# [[Программа:]] не нарцисс

while True:

    n=input("enter integer number in a range 0... 999 ")
    str_num=str(n)
    counter=len(n)
    check=0

    try:
        num=int(n)
    except:
        print('something went wrong')
        continue
    while num!=0:

        check=check+(num%10)**counter # at 1st step 0 + 153%10**3 =27
        num=num//10 #153//10=15

    if check==int(n):
        print('this is narcissistic number ')
    else: print('That is not narcissistic number . Pls. try again')


