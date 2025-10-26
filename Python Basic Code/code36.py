#Q36. Count vowels in string s = "hello"?

s = "hello"
count = 0
for c in s:
    if c in "aeiou":
        count += 1
print(count)