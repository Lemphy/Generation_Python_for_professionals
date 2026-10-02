# Более одного
# Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа, которые
# встречаются в данной последовательности более одного раза.

def more_than_one(string: str) -> list[int]:
    numbers = string.split()
    temp =  sorted(list(filter(lambda value: numbers.count(value) > 1,set(numbers))))
    return [int(value) for value in temp]

test = ['4 8 0 3 4 2 0 3',
        '1 2 3 4 5 4 5 6 7 7 7 7 4 4',
        '1 2 3 4 5 6 7 8 9',
        ]

for argument in test:
    print(*more_than_one(argument))