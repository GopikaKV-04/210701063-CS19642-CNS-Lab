def columnar_transposition_encrypt(plaintext, keyword):
    # Remove spaces from plaintext and convert to lowercase
    plaintext = plaintext.replace(" ", "").lower()
    keyword = keyword.lower()

    # Determine the order of columns based on the keyword
    keyword_order = sorted(list(keyword))
    num_cols = len(keyword)
    num_rows = -(-len(plaintext) // num_cols)  # Ceiling division

    # Pad plaintext to fit into the grid
    padded_plaintext = plaintext + ' ' * (num_cols * num_rows - len(plaintext))

    # Create the grid
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    # Fill the grid with characters from the plaintext
    for i, char in enumerate(padded_plaintext):
        row = i // num_cols
        col = i % num_cols
        grid[row][col] = char

    # Read the grid by columns in keyword order
    ciphertext = ''
    for key_char in keyword_order:
        col = keyword.index(key_char)
        for row in range(num_rows):
            ciphertext += grid[row][col]

    return ciphertext

def main():
    plaintext = input("Enter plaintext: ")
    keyword = input("Enter keyword: ")
    ciphertext = columnar_transposition_encrypt(plaintext, keyword)
    print("Encrypted text:", ciphertext)

if __name__ == "__main__":
    main()
