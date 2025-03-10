from pathlib import Path

# path = Path('programming.txt')

# path.write_text('i love programming1')

# name = input('Your name is ')

# path = Path('guets.txt')
# path.write_text(name)

# path = Path('guest_book.txt')

# while True:
#     name = input('Your name ')
#     if name != 'quit':
#         a = f'Hi {name}\n'
#         print(a)
#         path.write_text(a)
#     else:
#         break

from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nHi, what's your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)