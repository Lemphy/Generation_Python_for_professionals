# Функция filter_anagrams()
# Анаграммы — это слова, которые состоят из одинаковых букв. Например:
#
# адаптер — петарда
# адресочек — середочка
# азбука — базука
# аистенок — осетинка
# Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:
#
# word — слово в нижнем регистре
# words — список слов в нижнем регистре
# Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют анаграмму
# слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.

def filter_anagrams(word: str, words: list[str]) -> list[str]:
    temp = []
    if words:
        for value in words:
            if sorted(value) == sorted(word):
                temp.append(value)
        return temp
    else:
        return temp
    
word = ('abba',
        'отсечка',
        'tommarvoloriddle',
        'стекло',
        )

words = (['aabb', 'abcd', 'bbaa', 'dada'],
        ['сеточка', 'стоечка', 'тесачок', 'чесотка'],
        ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort'],
        [],
         )

for arg1, arg2 in zip(word, words):
    print(filter_anagrams(word = arg1, words = arg2))