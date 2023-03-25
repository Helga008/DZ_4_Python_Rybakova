# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

n = int(input('Введите количество дней в периоде '))
count_temp = 0 
count_max = 0

for i in range(n):
    tempr = int(input('Введите среднюю температуру за 1 день '))
    if tempr > 0:
        count_temp +=1
    elif count_temp != 0:
        if count_max < count_temp:
            count_max == count_temp
        count_temp = 0
if count_max < count_temp:
    count_max = count_temp
print(count_max)                    

