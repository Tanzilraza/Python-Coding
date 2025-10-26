#Q24. Write and read a file (write 'hi')
# with open("temp.txt","W") as  f: 
# f.write("hi")?

# Write 'hi' to a file
with open("temp.txt", "w") as f:
    f.write("hi")

# Read the content from the same file
with open("temp.txt", "r") as f:
    content = f.read()
    print(content)

