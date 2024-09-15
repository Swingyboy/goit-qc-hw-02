def create_playfair_matrix(keyword):
    matrix = []
    used_chars = set()
    for char in keyword.upper():
        if char not in used_chars and char.isalpha() and char != 'J':
            matrix.append(char)
            used_chars.add(char)
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None


def prepare_text(text):
    text = text.upper().replace('J', 'I')
    prepared = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared.append(text[i] + 'X')
            i += 1
        else:
            prepared.append(text[i] + (text[i + 1] if i + 1 < len(text) else 'X'))
            i += 2
    return prepared


def encrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def decrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def table_encrypt(text, keyword):
    matrix = create_playfair_matrix(keyword)
    prepared = prepare_text(text)
    encrypted = ''
    for pair in prepared:
        encrypted += encrypt_pair(matrix, pair[0], pair[1])
    return encrypted


def table_decrypt(text, matrix):
    matrix = create_playfair_matrix(matrix)
    prepared = prepare_text(text)
    decrypted = ''
    for pair in prepared:
        decrypted += decrypt_pair(matrix, pair[0], pair[1])
    return decrypted
