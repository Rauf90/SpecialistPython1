# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random
result_numbers = []
numbers = int(input("n: "))
for number in range(numbers):
    x = random.randint(-10, 10)
    result_numbers.append(x)
print(result_numbers)
positive_result_numbers = []
for result_number in result_numbers:
    if result_number > 0:
        positive_result_numbers.append(result_number)
print(sum(positive_result_numbers))
