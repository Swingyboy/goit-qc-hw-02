import string

from vigenere_encrypt import vigenere_decrypt, vigenere_encrypt
from permutation_encryption import single_decrypt, double_permutation_decrypt, double_permutation_encrypt, single_encrypt
from table_encrypt import table_decrypt, table_encrypt


def remove_punctuation(input_string):
    # Create a translation table that maps punctuation characters to None
    translator = str.maketrans('', '', string.punctuation)
    # Use the translation table to remove punctuation characters
    return input_string.translate(translator)


def task1(text):
    print("Task 1.\n Vigenere encryption and decryption.")
    vigenere_key = "CRYPTOGRAPHY"
    encrypted_text = vigenere_encrypt(text, vigenere_key)
    print(f"Vigenere encrypted text:\n {encrypted_text}")
    decrypted_text = vigenere_decrypt(encrypted_text, vigenere_key)
    print(f"Vigenere decrypted text:\n {decrypted_text}")
    print("=====================================\n")


def task2(text):
    print("Task 2.\n Single and double permutation encryption and decryption.")
    key_1 = "SECRET"
    key_2 = "CRYPTO"
    single_encrypted_text = single_encrypt(text, key_1)
    print(f"Single permutation encrypted text:\n {single_encrypted_text}")
    double_encrypted_text = double_permutation_encrypt(text, key_1, key_2)
    print(f"Double permutation encrypted text:\n {double_encrypted_text}")
    single_decrypted_text = single_decrypt(single_encrypted_text, key_1)
    print(f"Single permutation decrypted text:\n {single_decrypted_text}")
    double_decrypted_text = double_permutation_decrypt(double_encrypted_text, key_1, key_2)
    print(f"Double permutation decrypted text:\n {double_decrypted_text}")
    print("=====================================\n")


def task3(text):
    print("Task 3.\n Table encryption and decryption with Vigenere encryption and decryption.")
    keyword = "MATRIX"
    vigenere_keyword = "CRYPTO"
    encrypted_text = table_encrypt(text, keyword)
    print(f"Table encrypted text:\n {encrypted_text}")
    decrypted_text = table_decrypt(encrypted_text, keyword)
    print(f"Table decrypted text:\n {decrypted_text}")
    vigenere_encrypted_text = vigenere_encrypt(encrypted_text, vigenere_keyword)
    print(f"Vigenere encrypted table encrypted text:\n {vigenere_encrypted_text}")
    vigenere_decrypted_text = vigenere_decrypt(vigenere_encrypted_text, vigenere_keyword)
    decrypted_text = table_decrypt(vigenere_decrypted_text, keyword)
    print(f"Table decrypted Vigenere decrypted text:\n {decrypted_text}")
    print("=====================================\n")




def main():
    with open("input.txt") as f:
        lines = f.readlines()
        text_to_encrypt = lines[0].strip().upper().replace(" ", "")
        text_to_encrypt = remove_punctuation(text_to_encrypt)
        print(f"Text to encrypt: {text_to_encrypt}")
        print("=====================================\n")
        task1(text_to_encrypt)
        task2(text_to_encrypt)
        task3(text_to_encrypt)


if __name__ == "__main__":
    main()
