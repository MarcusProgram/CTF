file_path = 'task.txt'
binary_string = ''
with open(file_path, 'rb') as file:
    data = file.read()

for idx, byte in enumerate(data):
    if byte == 0x20:
        binary_string += '0'
    elif byte == 0xA0:
        binary_string += '1'

binary_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
flag = ''.join([chr(int(binary, 2)) for binary in binary_list])
print(flag)