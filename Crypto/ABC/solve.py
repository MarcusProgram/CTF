def get_letter(count):
    if 1 <= count <= 26:
        return chr(count + 96)
    else:
        return ""

with open('task', 'r') as file:
    lines = file.readlines()

for line in lines:
    count = line.count('-')
    letter = get_letter(count)
    print(letter,end='')