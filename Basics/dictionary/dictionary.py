# human = {
#     'first_name': 'egor',
#     'last_name': 'andrichuk',
#     'age': '27',
#     'city': 'st-peterburg',
# }
# print(human)

# numbers = {
#     'egor': '7',
#     'vlad': '14',
#     'andrey': '5',
#     'aleksandr': '7',
# } 

# print(numbers)

# glossariy = {
#     'lists': 'Изменяемый набор данных',
#     'typles': 'Неизменяемый набор данных',
#     'operators': 'Используется для вычисления',
#     'terms': 'Используется для упрощения кода',
# }


# for i in python:
    # print('\n', i, f': {python[i]}\n')

# for key, value in glossariy.items():
#     print(f'\nKey: {key}')
#     print(f'Value: {value}')

# glossariy['dict'] = 'Имеет пару ключ значение'    
# glossariy['len'] = 'Функция для измерения колличства символов'    
# glossariy['set'] = 'Множество, нужно для уникального списка без повторений'    

# for key, value in sorted(glossariy.items()):
#     print(f'\nKey: {key}')
#     print(f'Value: {value}')

# rivers = {
#     'moscow': 'Russia',
#     'temza': 'England',
#     'nile': 'Egypt',
# }

# for key in rivers.keys():
#     print(key)

# for value in rivers.values():
#     print(value)

# for k, v in rivers.items():
#     print(f'{k} протекает через {v}')

# peoples = ['jen', 'sarah', 'aleksandr', 'edward', 'phil', 'egor']

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for k in peoples:
#     if k in favorite_language:
#         print(f'Thank you for test, {k}')
#     else:
#         print(f'Plaese over tests, {k}')


# human_1 = {
#     'first_name': 'egor',
#     'last_name': 'andrichuk',
#     'age': '27',
#     'city': 'st-peterburg',
# }
# human_2 = {
#     'first_name': 'aleksandr',
#     'last_name': 'zdanov',
#     'age': '32',
#     'city': 'tumen',
# }
# human_3 = {
#     'first_name': 'andrey',
#     'last_name': 'gilmutdinov',
#     'age': '35',
#     'city': 'nojabrsk',
# }

# peoples = [human_1, human_2, human_3]

# for people in peoples:
#     print(people)

# favorite_places = {
#     'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
#     'erin': ['hawaii', 'iceland'],
#     'willie': ['mt. verstovia', 'the playground', 'new hampshire']
#     }

# for name, places in favorite_places.items():
#     print(f"\n{name.title()} likes the following places:")
#     for place in places:
#         print(f"- {place.title()}")



# numbers = {
#     'egor': ['1', '7'],
#     'vlad': ['14', '26'],
#     'andrey': ['699', '34'],
#     'aleksandr': ['4', '67'],
# } 

# for k,v in numbers.items():
#     print(f'\n{k.title()} his num is:')
#     for num in v:
#         print(f'{num}')


cites = {
    'moskow' : {
        'counntry' : 'russia',
        'population' : '15_000_000',
        'fact' : 'nice place',
    },
    'london' : {
        'counntry' : 'engalnd',
        'population' : '25_000_000',
        'fact' : 'the capital of great britian',
    },    
    'cair' : {
        'counntry' : 'egypt',
        'population' : '54_000_000',
        'fact' : 'oldest city',
    }

}

for city, setting in cites.items():
    print(f'{city.title()}:')
    for k, v in setting.items():
        print(f'\t{k} is {v}')