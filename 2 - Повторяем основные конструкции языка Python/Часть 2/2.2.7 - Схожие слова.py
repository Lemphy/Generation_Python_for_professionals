# Схожие слова
# Напишите программу, которая находит все схожие слова для заданного слова. Слова называются схожими, если имеют
# одинаковое количество и расположение гласных букв. При этом сами гласные могут различаться.

def similar_words(target: str, n: int, strings: tuple[str, ...]) -> list[str]:
    vowels = set('ауоыиэяюёе')
    result = []
    target_vowels = [index for index, char in enumerate(target) if char in vowels] # получили список из индексов гласных в target
    if not target_vowels: # если гласных в target не было обнаружено
        return result
    for string_index in range(0, n): # проходим кортеж строк
        string_vowels = [index for index, char in enumerate(strings[string_index]) if char in vowels] # получили список из индексов гласных в текущем string
        if target_vowels == string_vowels: # если индексы гласных совпали у обоих слов
            result.append(strings[string_index])
    return result

test = [('машина', 8, ('сеть', 'машинист', 'дорога', 'урок', 'работа', 'аксиома', 'железо', 'ветеран')),
        ('весть', 3, ('месть', 'гость', 'лань')),
        ]

for argument in test:
    print(*similar_words(*argument))