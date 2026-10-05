# Корпоративная почта 🌶️
# В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz,
# например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено
# приписывать справа номер.
#
# Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz, третий —
# timyr-guev2@beegeek.bzz, и так далее.
#
# Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде
# (латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

def corporate_email(count_use: int, use_emails: tuple[str, ...], count_new: int, new_names: tuple[str, ...]) -> list[str]:
    mail = '@beegeek.bzz'
    digits = '0123456789'
    use_names = list(use_name[:-len(mail)] for use_name in use_emails) # получили список занятых имен для почты
    #print('Список занятых имен', use_names)
    for new_name in new_names[:count_new]: # проходим кортеж новых имен для вставки
        len_new_name = len(new_name)
        find_names_without_numbers = set(name_without_numbers.rstrip(digits) for name_without_numbers in use_names) # смотрим есть ли у нас такое имя без конечных цифр, множество для устранения повторов
        #print('Имена без цифр:', find_names_without_numbers)
        #print('Искомое имя:', new_name)
        if new_name in find_names_without_numbers: # если было совпадение без учета цифр, значит имя уже имеется
            use_numbers = [] # список для занятых цифр
            for use_name in use_names: # проходим по занятых именах
                if new_name == use_name.rstrip(digits): # если новое имя равняется занятому без цифр
                    # добавляем последние цифры иначе если цифр нет 0
                    use_numbers.append(use_name[len_new_name:] if use_name[len_new_name:] else '0')
            #print('Список цифр', use_numbers)
            use_numbers = list(map(lambda x: int(x), use_numbers)) # проходим список преобразовав в числа
            use_numbers_max = max(use_numbers) # затем ищем наибольшее
            for i in range(use_numbers_max + 1): # ищем есть ли совпадения ДО максимального числа
                if i not in use_numbers: # если текущего i нет в списке занятых значений
                    if i == 0:
                        use_names.append(new_name) # если i = 0, значит имя первое, без цифры
                        break
                    else:
                        use_names.append(new_name + str(i)) # иначе записываем имя + его цифру
                        #print(f'Записали {new_name + str(i)}')
                        break
            else: # если завершился без break, значит все цифры заняты
                use_names.append(new_name + str(use_numbers_max + 1)) # записываем следующую цифру после MAX
        else: # совпадений нет, записываем новое имя без цифры
            use_names.append(new_name)
        #print('Обновленный список занятых имен', use_names)
    temp = list(map(lambda x: x + mail, use_names[-count_new:]))
    return temp

test = [(6,('ivan-petrov@beegeek.bzz',
            'petr-ivanov@beegeek.bzz',
            'ivan-petrov1@beegeek.bzz',
            'ivan-ivanov@beegeek.bzz',
            'ivan-ivanov1@beegeek.bzz',
            'ivan-ivanov2@beegeek.bzz',
          ),
         3,('ivan-ivanov',
            'petr-petrov',
            'petr-ivanov',
            )),
        (2,('timyr-guev2@beegeek.bzz',
            'anri-tabuev@beegeek.bzz',
            ),
         3,('timyr-guev',
            'timyr-guev',
            'anri-tabuev',
            )),
        ]

for argument in test:
    print(*corporate_email(*argument), sep = '\n')
    print()