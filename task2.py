# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import random

size = int(input("Введите количество кустов: "))

garden = [random.randint(1, 20) for i in range(1, size+1)]

print(garden)
result_list = list()
for i in range(len(garden) - 1):
    result_list.append(garden[i - 1] + garden[i] + garden[i + 1])
    print(result_list)
result_list.append((garden[-2]+garden[-1]+garden[0]))
print(max(result_list))
