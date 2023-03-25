# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

n = int(input('Введите размер списка'))
list_1 = []
for i in range(1,n+1):
    i = int(input('Введите значение списка'))
    list_1.append(i)
print(list_1)

list_2 = set(list_1)
print(len(list_2))

# m = 0
# count = 0

# if list_1[m+1] != list_1[m]:
#     count +=1
#     m += 1
# else:
#     m += 1    
# print(count)
