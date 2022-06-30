# *Задание:* Пользователь вводит в консоль слово на русском языке.
# Во введенном слове необходимо заменить символом
# ```-``` (дефис) все буквы, кроме гласных, и вывести результат в консоль.
#
# *Пример:*
# ```
# [Программа:] Введите слово:
# [Пользователь:] миллион
# [Программа:] -и--ио-
# ```
try:
    word=str(input('Введите слово:'))
except:
    print("Invalid input. Word should be string ")

vowels=["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", 'a', 'e', 'i', 'o', 'u']
for letter in word.lower():
    if letter not in vowels:
        word=word.replace(letter, "-")
print(word)




