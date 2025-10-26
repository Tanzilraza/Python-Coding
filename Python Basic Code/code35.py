#Q35. Palindrome number check n= 121?

n = 121
rev = 0
temp = n

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if n == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")
