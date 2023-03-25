# обозначение списков
list_1 = [1, 2, 3]
list_3 = []
list_2 = list()

for i in list_1:
    print(i)

# размер списка
print(len(list_1)) 

# обращение к элементу списка
print(list_1[0])
print(list_1[-2])

добавление значения в список
listok = [1, 3, 5, 9]
print(listok)
listok.append(8)
print(listok)

# программа для записи значения в список
list_1 = []
print(list_1)
for i in range(5):
    list_1.append(i)
    print(list_1)

Функции в списках
удаление последнего элемента
listok = [1, 3, 5, 9]
listok.pop()
print(listok)
# удаление конкретного элемента (указываем в скобках индекс)
listok.pop(0)
print(listok)
# добавление элемента на конкретную позицию
listok.insert(1,45)
print(listok)

срезы
listik = [1, 2, 4, 56, 54, 9, 0, 4, 45]
print(listik[:])
print(listik[3:])
print(listik[:5])
print(listik[2:-3])
# с шагом
print(listik[0:len(listik):6])





