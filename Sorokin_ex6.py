# Пользователь вводит в консоль целое неотрицательное число в пределах от 0 до 999.
# Необходимо вывести в консоль "антипод" введенного числа, то есть записать разряды задом наперед.
# При этом не разрешается использовать преобразование числа в строку.
# Пример:
# [Пользователь:] 532
# [Программа:] 235
while True:
    try:
        n=int(input('please, enter  number in a range of 0 ...999: '))
    except:
        print("Invalid input. Pls. check the format of input data. ")
        continue
    num=0

    while n!=0:
        remainder=n%10
        num=(num*10)+remainder
        n=n//10

    # Display the result
    print(f'The reversed number is: {num}')

