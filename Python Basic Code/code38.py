#Q38. Find LCM of two numbers?

a = 4
b = 6

# Find GCD first
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Then find LCM
lcm = (a * b) // gcd(a, b)
print(lcm)

'''a=12, b=18
GCD=6
LCM=(12*18)/6=36'''