# def display_message(message):
#     """выводит название раздела"""
#     print(f'Раздел {message}')

# display_message('функций')

# def favorite_book(title):
#     """выводит любимую книгу"""
#     print(f'одна из моих любимых книг "{title}"')

# favorite_book('Алиса в старне чудес')

# def make_short(size='L', text='I Love Python'):
#     print(f'Your shorts is {size} size and "{text}" on shorts')

# make_short('D', 'ILN')

# def descrive_city(city='Moskow', country='Russia'):
#     print(f'{city} is located in {country}')

# descrive_city()
# descrive_city('Oslo', 'Norvegia')
# descrive_city('St-petersburg')

# def city_country(city='moskow', country='russia'):
#     x = f"{city}, {country}"
#     return x.title()

# c = city_country('london', 'england')
# c = city_country('st.petersburg')
# print(c)

# def make_album(name, title, roads=''):
#     if not roads:
#         album = {'name': name.title(), 'title': title.title()}
#     else:
#         album = {'name': name.title(), 'title': title.title(), 'roads': roads}
#     return album

# alums = make_album('octin', 'nirvana', 5)
# print(alums)

# alums = make_album('octin', 'nirvana')
# print(alums)

# while True:
#     print('if exit enter q')
#     names = input('Name album ')
#     if names == 'q':
#         break
#     titles = input('Title albums ')
#     if titles == 'q':
#         break
#     m = make_album(names, titles, 6)
#     print(m)



# def show_message(messages):
#     for i in messages:
#         print(i)

def send_message(messages):
    while messages:
        current = messages.pop()
        print(current)
        sent_message.append(current)
    return sent_message

lists = ['hi, friends', 'hello, human', 'aloha']
sent_message = []

# show_message(lists[:])
send_message(lists[:])
print(lists)
print(sent_message)