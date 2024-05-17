def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher(ciphertext, -shift)

def main():
    plaintext = input("Enter plaintext: ")
    shift = 3 # Caesar cipher with a shift of 3
    ciphertext = caesar_cipher(plaintext, shift)
    print("Encrypted text:", ciphertext)
    decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
