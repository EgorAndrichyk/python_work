animals = ['cat', 'tiger', 'lion', 'dog', 'berd']

print(f'First elemtnts in list: {animals[:3]}')
print(f'Three elemtnts on centr in list: {animals[1:4]}')
print(f'Last elemtnts in list: {animals[3:]}')

new_animals = animals[:]

new_animals.append('sneak')

print(f'Animals is : {animals}')
print(f'new Animals is : {new_animals}')

for i in animals:
    print(i)

for i in new_animals:
    print(i)