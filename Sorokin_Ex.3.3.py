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
    word=str(input('Введите слово: \n'))
except:
    print("Invalid input. Word should be string")
upper_vowels=list()
vowels=["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", 'a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    upper_vowels.append(vowel.upper())

for letter in word:
    if letter not in vowels:
        if letter not in upper_vowels:
        #and not in upper_vowels
            word = word.replace(letter, "-")

print(word)





