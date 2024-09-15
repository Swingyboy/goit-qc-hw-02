def create_permutation(key):
    sorted_key = sorted(list(key))

    # Create a mapping from character to its position in the sorted key
    position_map = {}
    for i, char in enumerate(sorted_key):
        if char not in position_map:
            position_map[char] = []
        position_map[char].append(i + 1)

    # Generate the numerical sequence based on the original key
    numerical_sequence = []
    for char in key:
        numerical_sequence.append(position_map[char].pop(0))

    return numerical_sequence


def permute_block(text: str, permutation: list):
    block = {}
    for index, letter in zip(permutation, text):
        block[index] = letter
    return ''.join(letter for index, letter in sorted(block.items()))


def reverse_permute_block(text: str, permutation: list):
    original_block = {index + 1: letter for index, letter in enumerate(text)}
    block = [original_block.get(index, "") for index in permutation]
    return ''.join(block)


def single_encrypt(text, key):
    permutation = create_permutation(key)
    text += " " * (len(text) % len(key))
    blocks = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
    encrypted_blocks = [permute_block(block, permutation) for block in blocks]
    return ''.join(encrypted_blocks)


def single_decrypt(text, key):
    permutation = create_permutation(key)
    blocks = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
    decrypted_blocks = [reverse_permute_block(block, permutation) for block in blocks]
    return ''.join(decrypted_blocks)


def double_permutation_encrypt(text, key1, key2):
    text = single_encrypt(text, key1)
    text = single_encrypt(text, key2)
    return text


def double_permutation_decrypt(text, key1, key2):
    text = single_decrypt(text, key2)
    text = single_decrypt(text, key1)
    return text
