import random

def encode(s, num):
    result = ""
    for char in s:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
            shifted_index = (ord(char) - base + num) % 26 + base
            result += chr(shifted_index) 
        else:
            result += char
    return result

s = input("What is the string to be encoded? ")

num = input("Any specific shift in mind? ")

if isinstance(num, int):
    num%=26
else:
    num = random.randint(1, 25)

encoded_string = encode(s.upper(), num)
print(encoded_string)
