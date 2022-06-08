# Пользователь вводит в консоль целое число.
# Необходимо вывести в консоль последнюю цифру введенного числа (в десятичном представлении)
# При этом не разрешается использовать преобразование числа в строку.
while True:
    try:
        n=float(input('please, enter  number: '))
    except:
        print("Invalid input. Pls. check the format of input data. ")
        continue
    print(int(n%10))