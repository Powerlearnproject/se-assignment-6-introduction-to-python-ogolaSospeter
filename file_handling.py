# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    
# Writing to a file
lines = ["First line", "Second line", "Third line"]
with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")