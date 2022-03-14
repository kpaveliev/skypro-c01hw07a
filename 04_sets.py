
hat_wearers = {
    'Бычок',
    'Сельдь',
    'Лосось',
    'Скумбрия',
    'Толстолобик',
    'Карась'
}

walk_lovers = {
    'Карась',
    'Анчоус',
    'Карп',
    'Треска',
    'Лещ',
    'Лосось'
}

singers = {
    'Лещ',
    'Камбала',
    'Толстолобик',
    'Сельдь',
    'Бычок'
}

thinkers = {
    'Окунь',
    'Щука',
    'Осетр',
    'Бычок',
    'Сельдь',
    'Скумбрия'
}

print(
    f'Носят Шапочку и Любят гулять:\n'
    f'{chr(10).join(hat_wearers.intersection(walk_lovers))}'
    f'\nНосят Шапочку и Поют:\n'
    f'{chr(10).join(hat_wearers.intersection(singers))}'
    f'\nНосят Шапочку и Задумчивые:\n'
    f'{chr(10).join(hat_wearers.intersection(thinkers))}'
    f'\nЛюбят гулять и поют:\n'
    f'{chr(10).join(walk_lovers.intersection(singers))}'
    f'\nЛюбят гулять и Задумчивые:\n'
    f'{chr(10).join(walk_lovers.intersection(thinkers))}'
)

print('_______part 2_________')

print(
    f'Не Носят шапочку:\n'
    f'{chr(10).join(walk_lovers.union(singers, thinkers).difference(hat_wearers))}'
    f'\nНе Любят гулять:\n'
    f'{chr(10).join(hat_wearers.union(singers, thinkers).difference(walk_lovers))}'
    f'\nНе поют:\n'
    f'{chr(10).join(hat_wearers.union(walk_lovers, thinkers).difference(singers))}'
    f'\nНе задумчивые:\n'
    f'{chr(10).join(hat_wearers.union(walk_lovers, singers).difference(thinkers))}'
)