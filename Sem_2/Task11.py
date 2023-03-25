# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765

number = int(input('Введите число '))
number0 = 0
number1 = 1 
count = 2
key = True
while key:
    numberFib = number0 + number1
    if numberFib < number:
        number0 = number1
        number1 = numberFib
        count += 1
    elif numberFib == number:
        count += 1
        key = False
    else:
        count = -1
        key = False
print(count)                           

