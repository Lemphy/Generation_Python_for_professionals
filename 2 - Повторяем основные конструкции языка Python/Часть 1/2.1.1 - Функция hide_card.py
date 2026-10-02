# Функция hide_card()
# Реализуйте функцию hide_card(), которая принимает один аргумент:
#
# card_number — строка, представляющая собой корректный номер банковской карты из 16 цифр, между которыми могут
# присутствовать символы пробела
# Функция должна заменять первые 12 цифр в строке card_number на символ * и возвращать полученный результат. Если между
# цифрами в номере имелись символы пробела, их следует удалить.

def hide_card(card_number: str) -> str | None:
    card_number = [char for char in card_number if char.isdigit()]
    if len(card_number) == 16:
        temp = ['*' for char in card_number[:-4]] + card_number[-4:]
        return ''.join(temp)
    else:
        return None

cards = ['3456 9012 5678 1234',
         '1234567890123456',
         '905 678123 45612 56',
         ]

for result in cards:
    print(f'Входные данные: {result}\n'
          f'Результат: {hide_card(result)}')
