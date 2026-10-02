# Функция print_given()
# Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов и
# выводит все переданные аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться каждая на отдельной
# строке, в следующем формате:
#
# для позиционных аргументов:
# <значение аргумента> <тип аргумента>
# для именованных аргументов:
# <имя переменной> <значение аргумента> <тип аргумента>

def print_given(*args, **kwargs):
    if args:
        for value in args:
            print(f'{value} {type(value)}')

    if kwargs:
        for key, value in sorted(kwargs.items()):
            print(f'{key} {value} {type(value)}')
    return None

print_given(1, [1, 2, 3], 'three', two=2)
print()
print_given('apple', 'cherry', 'watermelon')
print()
print_given(b=2, d=4, c=3, a=1)
