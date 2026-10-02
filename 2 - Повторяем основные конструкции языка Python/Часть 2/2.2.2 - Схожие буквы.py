# Схожие буквы
# В русском и английском языках есть буквы, которые выглядят одинаково. Вот список английских букв
# "AaBCcEeHKMOoPpTXxy", а вот их русские аналоги "АаВСсЕеНКМОоРрТХху". Напишите программу, которая для трёх букв из
# данных списков букв определяет, русские они, английские или и те и другие (смесь русских и английских букв).

def similar_letters(arg: tuple[str, ...]) -> str | None:
    russian = "АаВСсЕеНКМОоРрТХху"
    english = "AaBCcEeHKMOoPpTXxy"
    temp = [0,0]
    result = None
    for char in arg:
        if char in russian: # является ли char подстрокой russian
            temp[0] += 1 # прибавляем в счетчик
        elif char in english: # является ли char подстрокой english
            temp[1] += 1 # прибавляем в счетчик
    if temp[0] > 0 and temp[1] > 0: # если значения обох ячеек больше нуля
        result = 'mix'
    elif temp[0] > 0:
        result = 'ru'
    elif temp[1] > 0:
        result = 'en'
    return result

test = [('Р', 'О', 'А'),
        ('O', 'K', 'M'),
        ('T', 'a', 'В'),
        ]

for argument in test:
    print(similar_letters(argument))