import random

# class Die:

#     def __init__(self, side=6):
#         self.side = side

#     def roll_die(self):
#         print(random.randint(1, self.side))

# a = Die(20)
# a.roll_die()


lists = ['f', 23, 2, 4, 'a', 'h', 'y', 10, 'j', 'a', 7, 'o', 'u', 'l']

# i = 1
# winner = ''

# while i < 5:
#     a = random.choice(lists)
#     winner+=str(a)
#     i+=1

# print(f'Победитель с номером {winner}')

# for _ in range(4):
#     a = random.choice(lists)
#     winner += str(a) + ' '

# print(f'Победитель с номером {winner.strip()}')

# winners = random.sample(lists, 4)

my_ticket = [4, 'h', 'y', 10]

# i=0

# while my_ticket != winners:
#     winners = random.sample(lists, 4)
#     i+=1

attempts = 0

while True:
    winners = random.sample(lists, 4)
    attempts += 1
    if winners == my_ticket:
        break

print(attempts)