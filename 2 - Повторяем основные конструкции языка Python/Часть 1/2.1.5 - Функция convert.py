# Функция convert()
# Реализуйте функцию convert(), которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать строку string:
#
# полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
# полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
# полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает

def convert(string: str) -> str:
    lower = 0
    upper = 0
    for char in string:
        if char.isalpha():
            if char.islower():
                lower += 1
            else:
                upper += 1
    return string.lower() if lower >= upper else string.upper()

test = ['BEEgeek',
        'pyTHON',
        'pi31415!',
        ]

for argument in test:
    print(convert(argument))

