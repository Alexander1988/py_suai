#Пользователь вводит в консоль три целых положительных числа:
#количество часов
#количество минут
#количество секунд
#Необходимо вывести общее число секунд.

import time


while True:
    hrs=input('pls. enter how many hours passed: ')

    if hrs == "done" :
        break
    mins=input('pls. enter how many minutes passed: ')
    secs=input('pls. enter how many seconds passed: ')
    time.sleep(0.5)

    try:
        h=int(hrs)
        m=int(mins)
        s=int(secs)
    except:
        #if input invlaid inform user
        print("Invalid input. Pls. enter integer number")
        continue
    print('to finish program type "done"')
    total_time_in_secs=h*3600+m*60+s
    print('The total time in secs passed: '+str(total_time_in_secs))
    time.sleep(0.5)



