#Пользователь вводит в консоль три целых положительных числа:
#количество часов
#количество минут
#количество секунд
#Необходимо вывести общее число секунд.

import time


while True:
    try:
        hrs,mins,secs=input('pls. enter how many hours, minutes and seconds passed in the following format: hh mm ss: ').split()
        h=int(hrs)
        m=int(mins)
        s=int(secs)
    except:
        print("Invalid input. Pls. check the format. You should use spaces between integer numbers. ")
        continue

    print('to finish program type "done"')
    total_time_in_secs=h*3600+m*60+s
    print('The total time in secs passed: '+str(total_time_in_secs))
    time.sleep(2)
    ans=input('Finish this program? y/n: ')
    if ans == "y" :
        break
    time.sleep(0.5)



