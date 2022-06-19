# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())  # Первое число
second_number = int(input())  # Второе число
list_kratno_3 = []
for number in range(first_number, second_number):
    if number % 3 == 0:
        list_kratno_3.append(number)
print(list_kratno_3)
