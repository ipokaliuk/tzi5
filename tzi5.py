def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

numbers = [
    (26325, 42315),
    (391951, 161063),
    (221867, 301971),
    (2004687, 5127506)
]

for a, b in numbers:
    print(f"НСД({a}, {b}) = {gcd(a, b)}")
