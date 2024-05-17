def prime_checker(p):
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

def primitive_check(g, p):
    # Check if g is a primitive root modulo p
    residues = set()
    for i in range(1, p):
        residues.add(pow(g, i, p))
    return len(residues) == p - 1

def get_input(prompt, condition):
    while True:
        value = int(input(prompt))
        if condition(value):
            return value
        print("Invalid input, please try again.")

def diffie_hellman_key_exchange():
    P = get_input("Enter P (prime number): ", prime_checker)
    G = get_input(f"Enter a primitive root of {P}: ", lambda x: primitive_check(x, P))

    x1 = get_input("Enter the private key of User 1: ", lambda x: 0 < x < P)
    x2 = get_input("Enter the private key of User 2: ", lambda x: 0 < x < P)

    y1 = pow(G, x1, P)
    y2 = pow(G, x2, P)

    k1 = pow(y2, x1, P)
    k2 = pow(y1, x2, P)

    print(f"\nSecret Key for User 1: {k1}\nSecret Key for User 2: {k2}\n")

    if k1 == k2:
        print("Keys have been exchanged successfully.")
    else:
        print("Keys have not been exchanged successfully.")

if __name__ == "__main__":
    diffie_hellman_key_exchange()
