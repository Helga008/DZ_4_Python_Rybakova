# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза / Input: 5 -> 5 1 6 5 9 Output: 1 9

from random import randint
n = int(input('Введите количество арбузов '))
min_weight = 50
max_weight = 0
i = 0
while i < n:
    weight = randint(1,10)
    print(weight)
    if weight < min_weight:
        min_weight = weight

    elif weight > max_weight:
        max_weight = weight
    i+=1
print()
print(min_weight, max_weight)            

    


