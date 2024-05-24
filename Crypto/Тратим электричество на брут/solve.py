import base64


def xor_decrypt(data, key):
    key = key.encode()
    decrypted = ''
    for i in range(len(data)):
        decrypted += chr(data[i] ^ key[i % len(key)])
    return decrypted


encoded_string = "cUATQBhRVUBBFFJfWVMUHhhZR1tIT1ZBTUAHbEwAR1hLawBBC2tZVlBJ"
decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode()

for i in range(10000):
    key = str(i).zfill(4)
    decrypted = xor_decrypt(decoded_bytes, key)
    if 'mshp{' in decrypted:
        print(decrypted)