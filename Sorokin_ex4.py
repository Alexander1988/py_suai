# Пользователь вводит в консоль целое положительное число n.
# Необходимо вычислить выражение "n в кубе плюс два n"
# и вывести в консоль текст "True", если результат кратен трём
# или "False", если некратен.
# При этом не разрешается использовать условный оператор if - else.
# Подсказка: используйте оператор сравнения "==".

while True:
    try:
        n=int(input('please, enter integer number: '))
    except:
        print("Invalid input. Pls. check the format of input data. You should use integer numbers. ")
        continue
    eq=(n**3)+2*n #our expression
    print(eq%3==0) #script prints out result and checks remainder by dividing it to 3