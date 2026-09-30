# Функция get_biggest()
# Реализуйте функцию get_biggest(), которая принимает один аргумент:
#
# numbers — список целых неотрицательных чисел
# Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers. Если список numbers
# пуст, функция должна вернуть число −1.

def get_biggest(numbers):
    if not numbers:
        return -1

    # Переводим всё в строки
    nums = [str(x) for x in numbers]
    n = len(nums)

    # Сортировка пузырьком через циклы for
    for i in range(n):
        for j in range(n - 1 - i):
            # Сравниваем: если сложить nums[j] + nums[j+1] меньше,
            # чем nums[j+1] + nums[j], меняем их местами
            if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(nums)
    # Теперь можно собрать через строку-аккумулятор!
    acc = ""
    for s in nums:
        acc += s

    return int(acc)


print(get_biggest([1, 2, 3]))