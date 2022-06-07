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
    schilling=Penny//12 #int number
    Pound_sterling=schilling//20 #int number

    print(f'the number of penny you is equivalent to  {Pound_sterling} Pounds, or {schilling} schillings, or {Penny} Pennies') #print out results

