# Функция choose_plural() 🌶️🌶️
# Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:
#
# amount — натуральное число, количество
# declensions — кортеж из трех вариантов склонения существительного
# Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа declensions и
# количества amount, в следующем формате:
#
# <количество> <существительное>

def choose_plural(amount: int, declensions: tuple[str, ...]) -> str:
    if amount % 100 in range(11,15):
        index = 2
    else:
        temp = amount % 10
        if temp == 0 or temp >= 5:
            index = 2
        elif temp >= 2:
            index = 1
        else:
            index = 0

    return f'{amount} {declensions[index]}'

test = [(2, ('пример', 'примера', 'примеров')),
        (14, ('гвоздь', 'гвоздя', 'гвоздей')),
        (8, ('яблоко', 'яблока', 'яблок')),
        ]

for argument in test:
    print(choose_plural(*argument))