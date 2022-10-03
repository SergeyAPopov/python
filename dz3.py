# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list1 = [2, 3, 5, 9, 3]
count = 0
for i in range(len(list1)):
    if i % 2 != 0: count+= list1[i]
print('Сумма значений на нечетных позициях:', count)


# '2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
count = len(list1) /2
for i in range(len(list1)):
    if i < count:
        print(list1[i] * list1[-(i+1)])



# '3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5, 10.01]
list2= []
for i in range(len(list1)):
    if round(list1[i] - int(list1[i]), 2) != 0:
        list2.append(round(list1[i] - int(list1[i]), 2))
print(max(list2) - min(list2))

# '4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

numberin = str(bin(int(input('Введите число: '))))
result = numberin.replace('0b', ' ')
print('Указаное число в двоичной системе: ', result)
