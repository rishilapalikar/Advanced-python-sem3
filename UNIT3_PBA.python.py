import re

with open("input.txt", "r") as file:
    text = file.read()

text = re.sub(r' {2,}', ' ', text)

with open("input.txt", "w") as file:
    file.write(text)

print("Multiple spaces replaced with a single space.")