moto = 'yamaha'

print('is moto== "yamaha"? i predict True')
print(moto == 'yamaha')

print('\nis moto == "bmw"? i predict False')
print(moto == 'bmw')

games = ['diablo', 'call of duty', 'portal', 'dota', 'cs']

if games[0] == games[1]:
    print('its good')
else:
    print('not good')

if 'diablo' in games:
    print('good')
else:
    print('not in list')

if 'diablo' not in games:
    print('good')
else:
    print('not in list')
    
a = 10
b = 15
c = 14 

if a > b or b < c:
    print('+')
else:
    print('-')