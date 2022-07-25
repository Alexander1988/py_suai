# *Задание:* Пользователь вводит предложение произвольной длины, удовлетворяющее следующим условиям:
# Первое слово начинается с заглавной буквы.
# Все буквы в предложении кроме первой буквы первого слова - строчные.
# Знаки препинания в середине предложения отсутствуют, в конце ставится точка.
# Программа переставляет слова в обратном порядке и выводит получившееся предложение.
# Выведенное предложение должно удовлетворять тем же условиям, что исходное.
#
# *Примечание:* Если пользователь вводит пустую строку, программа также должна выводить пустую строку.
#
# *Пример:*
# ```
# [Программа:] Введите предложение
# [Пользователь:] Вол ждал воды.
# [Программа:] Воды ждал вол.
# `
import re
import sys
sent=input('Введите предложение \n')
sent=re.sub(r'[^\w\s]','', sent)
if len(sent) == 0:
    print("\n"*1)
else:
    res=[]
    new_sent=[]
    i=1 #counter for words in a new sentence

    #forming a list with a words in reverse order
    for word in sent.split():
        if word.endswith('.'):
            word=word[:-1]
        res.append(word)
    res=' '.join(res[::-1]).lower() #making all words in a list are lower

    num_words=len(re.findall(r'\w+', res)) #how many words in a list

    #forming new sentence
    for new_word in res.split():
        if i == 1:
            new_word=new_word.capitalize() #according to the task the first word should has capitalized first letter
        elif i == num_words:
            new_word=''.join((new_word,'.')) #according to the task the last word should has a dot symbol at the end
        new_sent.append(new_word)
        i +=1 #incremntation of words counter
    new_sent =' '.join(new_sent)
    print(new_sent)




