# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число. 
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

list_1 = [elem for elem in range(int(input('Введите размер списка')))]
print(list_1)

k = int(input('Введите положительно число '))

list_2 = list(list_1[len(list_1) - k : len(list_1) : 1])
print(list_2)

list_3 = list(list_1[0 : (len(list_1) - k)])
print(list_3)

print(list_2 + list_3)