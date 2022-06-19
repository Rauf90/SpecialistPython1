# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random
result_numbers = []
numbers = int(input("n: "))
for number in range(numbers):
    x = random.randint(-10, 10)
    result_numbers.append(x)
print(result_numbers)
sum_result_numbers = sum(result_numbers)
print(sum_result_numbers)
