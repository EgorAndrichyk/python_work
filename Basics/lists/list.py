# bycycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(f"my first bycycle was a {bycycles[-1].title()}")

names = ['Andrey', 'Vlad', 'Aleksandr']
# print(names[0])
# print(names[1])
# print(names[2])

message = f"Hi my friend, {names[0]}"
message1 = f"Hi my friend, {names[1]}"
message2 = f"Hi my friend, {names[2]}"
print(message)
print(message1)
print(message2)

message = f"Hi my friend {names[0]}, are you going to dinner?"
message1 = f"Hi my friend {names[1]}, are you going to dinner?"
message2 = f"Hi my friend {names[2]}, are you going to dinner?"
print(message)
print(message1)
print(message2)

print(f"{names[0]} won't be able to come")

names[0] = 'Artem'
print(names)

message = f"Hi my friend {names[0]}, are you going to dinner?"
message1 = f"Hi my friend {names[1]}, are you going to dinner?"
message2 = f"Hi my friend {names[2]}, are you going to dinner?"

print(message)
print(message1)
print(message2)

print('I found a bigger table')

names.insert(0, 'Anastasia')
names.insert(1, 'Sergey')
names.append('Egor')

print(names)

message = f"Hi my friend {names[0]}, are you going to dinner?"
message1 = f"Hi my friend {names[1]}, are you going to dinner?"
message2 = f"Hi my friend {names[2]}, are you going to dinner?"
message3 = f"Hi my friend {names[3]}, are you going to dinner?"
message4 = f"Hi my friend {names[4]}, are you going to dinner?"
message5 = f"Hi my friend {names[5]}, are you going to dinner?"

print(message)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)

print('two are invited')

print(f'sorry {names[5]}')
first_guest = names.pop(5)
print(names)

print(f'sorry {names[3]}')
first_guest = names.pop(3)
print(names)

print(f'sorry {names[1]}')
first_guest = names.pop(1)
print(names)

print(f'sorry {names[0]}')
first_guest = names.pop(0)
print(names)

del names[0]
del names[0]

print(names)