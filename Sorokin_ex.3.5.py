# *Задание:* Пользователь вводит в консоль слова по одному.
# Когда пользователь вводит пустую строку, программа выводит
# в консоль слово, составленное из первых букв введенных слов
# и завершает работу.
#
# *Пример:*
# ```
# [Программа:] Вводите слова по одному, для окончания введите пустую строку:
# [Пользователь:] слон
# [Пользователь:] огурец
# [Пользователь:] рыба
# [Пользователь:] орех
# [Пользователь:] кот
# [Пользователь:] арбуз
# [Пользователь:]
# [Программа:] сорока
# ```

word=None
lst=list()
while word!="":
    word=str(input('Вводите слова по одному, для окончания введите пустую строку: '))
    if word!='':
        lst.append(word[0])


print(''.join(lst))