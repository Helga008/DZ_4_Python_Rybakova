# создать список, состоящий из чётных чисел в диапазоне от 1 до 100

list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)   

# Эту же функцию можно написать проще

list_2 = [i for i in range(1, 101)]
print(list_2)