# Функция choose_plural() 🌶️🌶️
# Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:
#
# amount — натуральное число, количество
# declensions — кортеж из трех вариантов склонения существительного
# Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа declensions и
# количества amount, в следующем формате:
#
# <количество> <существительное>
TWO = 2
FIVE = 5

def choose_plural(amount: int, declensions: tuple[str, ...]) -> str:
    temp = amount % 10
    if temp == 0:
        temp = FIVE

    if temp >= FIVE:
        return f'{amount} {declensions[2]}'
    elif temp >= TWO:
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[0]}'

test = [(21, ('пример', 'примера', 'примеров')),
        (100, ('гвоздь', 'гвоздя', 'гвоздей')),
        (8, ('яблоко', 'яблока', 'яблок')),
        ]

for argument in test:
    print(choose_plural(*argument))