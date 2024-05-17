def prepare_key(key):
    key = key.replace("j", "i")
    key_set = []
    for char in key:
        if char not in key_set:
            key_set.append(char)
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # Excluding 'j'
    key_square = "".join(key_set)
    for char in alphabet:
        if char not in key_square:
            key_square += char
    return key_square

def generate_key_square(key):
    key_square = prepare_key(key)
    key_matrix = [key_square[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix

def find_position(char, key_square):
    for i, row in enumerate(key_square):
        if char in row:
            return i, row.index(char)

def encrypt(plaintext, key):
    key_square = generate_key_square(key)
    plaintext = plaintext.replace("j", "i")
    
    # Prepare plaintext pairs
    plaintext_pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'x'
        if a == b:
            b = 'x'
        else:
            i += 1
        plaintext_pairs.append(a + b)
        i += 1
    
    ciphertext = ""
    for pair in plaintext_pairs:
        row1, col1 = find_position(pair[0], key_square)
        row2, col2 = find_position(pair[1], key_square)
        if row1 == row2:
            ciphertext += key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_square[row1][col2] + key_square[row2][col1]
    return ciphertext

def main():
    key = input("Enter key: ").lower()
    plaintext = input("Enter plaintext: ").lower().replace(" ", "")
    key_square = generate_key_square(key)
    print("Key Square:")
    for row in key_square:
        print(" ".join(row))
    ciphertext = encrypt(plaintext, key)
    print("\nEncrypted text:", ciphertext)

if __name__ == "__main__":
    main()
