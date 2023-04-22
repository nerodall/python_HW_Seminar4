# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в
# порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
#  — кол-во элементов первого множества.
#  — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random

size_of_first_list = int(input("Введите размер первого списка: "))

size_of_second_list = int(input("Введите размер второго списка: "))

first_list = {random.randint(1, 20) for i in range(1, size_of_first_list)}
second_list = {random.randint(1, 20) for j in range(1, size_of_second_list)}
print(first_list)
print(second_list)

result_list = first_list.intersection(second_list)
result_list = list(result_list)
result_list.sort()
print(result_list)
