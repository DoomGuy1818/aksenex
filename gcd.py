def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        print(a)
    return a

gcd(32, 54)