# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32

class1 = int(input('Введите кол-во учащихся в 1 классе '))
class2 = int(input('Введите кол-во учащихся в 2 классе '))
class3 = int(input('Введите кол-во учащихся в 3 классе '))
sum = class1 + class2 + class3
parts = int(sum / 2 + sum % 2)
print(f'Нужно {parts} парт')