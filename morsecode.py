morse = {
    ' ' : "/",
    'A' : ".-",
    'B' : "-...",
    'C' : "-...",
    'D' : "-..",
    'E' : ".",
    'F' : "..-.",
    'G' : "--.",
    'H' : "....",
    'I' : "..",
    'J' : ".---",
    'K' : "-.-",
    'L' : ".-..",
    'M' : "--",
    'N' : "-.",
    'O' : "---",
    'P' : ".--.",
    'Q' : "--.-",
    'R' : ".-.",
    'S' : "...",
    'T' : "-",
    'U' : ".-",
    'V' : "...-",
    'W' : ".--",
    'X' : "-..-",
    'Y' : "-.--",
    'Z' : "--..",
    '.' : "-.-.-",
    ',' : "--..--",
    '?' : "..--..",
    '/' : "-..-.",
    '@' : ".--.-.",
    '1' : ".----",
    '2' : "..---",
    '3' : "...--",
    '4' : "....-",
    '5' : ".....",
    '6' : "-....",
    '7' : "--...",
    '8' : "---..",
    '9' : "----.",
    '0' : "-----",

}

def encode(s):
    m = ""
    for char in s:
        char = morse[char]
        m = m + char
    return m

def decode(s):
    m = ""
    return m


# print("Please do enter '/' for giving space between words") #give warning for decoding
s = input("What is the string to be encoded?\n")
s = s.upper()
print(encode(s))