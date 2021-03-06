# ### 5.1 Кто в теремочке живёт?
#
#
# *Задание:* Пользователь вводит имена животных, живущих в теремке,
# через пробел по одному.
# Животные могут повторяться. В конце пользователь нажимает "Ввод".
# Программа выводит неповторяющиеся имена животных, написанные с большой буквы,
# между именами ставится союз "и" с точкой в конце.
# Если имя только одно, союз не ставится.
#
# *Условие:* Пользователь вводит имена в любом регистре.
# Программа при определении неповторяющихся имен игнорирует регистр (см. пример).
# Порядок ввода имен должен сохраняться.
#
# *Примечание:* Обязательно использовать множества (set).
#
# *Пример:*
# ```
# [Программа:] Кто в теремочке живёт?
# [Пользователь:] мышка жучка МЫШКА лиса заяц Заяц заяЦ волк.
# [Программа:] Мышка и Жучка и Лиса и Заяц и Волк.
# ```

user_words = input('Кто в теремочке живёт?\n').split()
last_word = user_words[-1]

output = []
for word in user_words:
    if word == last_word and not last_word.endswith("."):
        word=''.join((word,'.'))
    elif len(user_words) == 1:
        word=''.join((word,'.'))
    word = word.lower().capitalize()
    output.append(word)

res = " и ".join(sorted(set(output), key=output.index))
print(res)

