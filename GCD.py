def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print("Введите два числа поочерёдно")

a = int(input())
b = int(input())

print(gcd(a, b))