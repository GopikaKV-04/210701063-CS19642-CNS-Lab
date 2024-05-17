import math

def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

def generate_keypair(p, q):
    n = p * q
    totient = (p - 1) * (q - 1)
    e = 2
    while e < totient:
        if gcd(e, totient) == 1:
            break
        else:
            e += 1
    d = modinv(e, totient)
    return ((e, n), (d, n))

def rsa_encrypt(msg, public_key):
    e, n = public_key
    c = pow(msg, e, n)
    return c

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    m = pow(ciphertext, d, n)
    return m

def main():
    p = int(input("Enter prime1: "))
    q = int(input("Enter prime2: "))
    public_key, private_key = generate_keypair(p, q)
    print("Public key:", public_key)
    print("Private key:", private_key)

    msg = int(input("Enter message: "))
    print("Original Message:", msg)

    ciphertext = rsa_encrypt(msg, public_key)
    print("Encrypted Data:", ciphertext)

    decrypted_msg = rsa_decrypt(ciphertext, private_key)
    print("Decrypted Message:", decrypted_msg)

if __name__ == "__main__":
    main()
