def rail_fence_cipher(plaintext, rails):
    if rails == 1:
        return plaintext

    # Create a list of strings for each rail
    rail = ['' for _ in range(rails)]
    direction_down = False
    row = 0

    # Traverse through the plaintext
    for ch in plaintext:
        rail[row] += ch
        
        # Change direction if we hit the top or bottom rail
        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        # Move to the next rail
        row += 1 if direction_down else -1

    # Combine all rails to get the ciphertext
    return ''.join(rail)

def main():
    plaintext = input("Enter plaintext: ")
    rails = int(input("Enter number of rails: "))
    ciphertext = rail_fence_cipher(plaintext, rails)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
