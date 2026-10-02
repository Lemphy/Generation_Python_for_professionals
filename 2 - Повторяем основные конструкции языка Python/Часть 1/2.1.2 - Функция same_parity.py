# Функция same_parity()
# Реализуйте функцию same_parity(), которая принимает один аргумент:
# numbers — список целых чисел
# Функция должна возвращать новый список, элементами которого являются числа из списка numbers, имеющие ту же четность,
# что и первый элемент этого списка.


def same_parity(number: list[int]) -> list[int]:
    return list(filter(lambda value: value % 2 == number[0] % 2,number)) if number else number

test = [[],
        [6, 0, 67, -7, 10, -20],
        [-7, 0, 67, -9, 70, -29, 90],
        ]

for argument in test:
    print(same_parity(argument))
