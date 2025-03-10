from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)
# lines = contents.splitlines()
pi_list = []

for list in contents.splitlines():
    pi_list.append(list.replace('python', 'C'))

print(pi_list)