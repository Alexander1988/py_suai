# Напишите программу
# В одном фунте стерлингов - 20 шиллингов
# В одном шиллинге - 12 пенсов
# Пользователь вводит в консоль число пенсов.
# Необходимо вывести эквивалентное число фунтов, шиллингов и пенсов.

#define all variables
while True:
    try:
        Penny=int(input('please, write down how many penny you have: '))
    except:
        print("Invalid input. Pls. check the format of input data. You should use integer numbers. ")
        continue

    Pound_sterling=Penny//240#int number of pounds
    Schilling=(Penny%240)//12
    Users_penny=(Penny%240)%12
    print(f'you have a {Pound_sterling} Pounds, {Schilling} schillings, and {Users_penny} Pennies') #print out results

