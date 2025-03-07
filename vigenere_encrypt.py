def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def vigenere_encrypt(text, key):
    encrypted_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypted_text.append(chr(x))
    return "".join(encrypted_text)


def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key = generate_key(encrypted_text, key)
    for i in range(len(encrypted_text)):
        x = (ord(encrypted_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        decrypted_text.append(chr(x))
    return "".join(decrypted_text)

