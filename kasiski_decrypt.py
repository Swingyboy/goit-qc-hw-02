import re
from collections import defaultdict, Counter
import math
import string


def find_repeating_sequences(ciphertext, min_length=3):
    sequences = defaultdict(list)
    length = len(ciphertext)

    for seq_len in range(min_length, length // 2 + 1):
        for i in range(length - seq_len):
            seq = ciphertext[i:i + seq_len]
            if seq in sequences:
                sequences[seq].append(i)
            else:
                sequences[seq] = [i]

    repeating_sequences = {seq: positions for seq, positions in sequences.items() if len(positions) > 1}
    return repeating_sequences


def calculate_distances(positions):
    distances = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            distance = abs(positions[j] - positions[i])
            distances.append(distance)
    return distances


def find_common_divisors(distances):
    divisors = defaultdict(int)
    for distance in distances:
        for i in range(1, int(math.sqrt(distance)) + 1):
            if distance % i == 0:
                divisors[i] += 1
                divisors[distance // i] += 1
    return sorted(divisors.items(), key=lambda x: x[1], reverse=True)


def kasiski_examination(ciphertext):
    repeating_sequences = find_repeating_sequences(ciphertext)
    all_distances = []

    for seq, positions in repeating_sequences.items():
        distances = calculate_distances(positions)
        all_distances.extend(distances)

    common_divisors = find_common_divisors(all_distances)

    return [divisor for divisor, count in common_divisors]


def decrypt_vigenere(ciphertext, key):
    alphabet = string.ascii_uppercase
    key = key.upper()
    key_length = len(key)
    decrypted_text = []

    for i, char in enumerate(ciphertext):
        if char in alphabet:
            key_char = key[i % key_length]
            shift = alphabet.index(key_char)
            new_char = alphabet[(alphabet.index(char) - shift) % 26]
            decrypted_text.append(new_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


def frequency_analysis(segment):
    alphabet = string.ascii_uppercase
    frequencies = Counter(segment)
    most_common = frequencies.most_common(1)[0][0]
    shift = (alphabet.index(most_common) - alphabet.index('E')) % 26
    return shift


def break_vigenere(ciphertext, key_length):
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())
    segments = [''.join(ciphertext[i::key_length]) for i in range(key_length)]
    key = ''

    for segment in segments:
        shift = frequency_analysis(segment)
        key += string.ascii_uppercase[shift]

    return key


def kasiski_and_decrypt(ciphertext):
    possible_key_lengths = kasiski_examination(ciphertext)
    print("Possible Key Lengths:", possible_key_lengths)

    for length in possible_key_lengths:
        print(f"\nTrying key length: {length}")
        key = break_vigenere(ciphertext, length)
        print(f"Guessed Key: {key}")
        decrypted_text = decrypt_vigenere(ciphertext, key)
        print(f"Decrypted Text:\n{decrypted_text}")

