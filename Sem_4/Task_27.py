# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов cодержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

stroka = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells seashells on the sea shore I'm sure that the shells are sea shore shells"
spisok = list(stroka.upper().split())
print(spisok)

new_sp = set(spisok)
print(len(new_sp))

