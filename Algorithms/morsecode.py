morse = {
    ' ' : "/",
    'A' : ".- ",
    'B' : "-... ",
    'C' : "-.-. ",
    'D' : "-.. ",
    'E' : ". ",
    'F' : "..-. ",
    'G' : "--. ",
    'H' : ".... ",
    'I' : ".. ",
    'J' : ".--- ",
    'K' : "-.- ",
    'L' : ".-.. ",
    'M' : "-- ",
    'N' : "-. ",
    'O' : "--- ",
    'P' : ".--. ",
    'Q' : "--.- ",
    'R' : ".-. ",
    'S' : "... ",
    'T' : "- ",
    'U' : "..- ",
    'V' : "...- ",
    'W' : ".-- ",
    'X' : "-..- ",
    'Y' : "-.-- ",
    'Z' : "--.. ",
    '\'': ".----. ",
    '(' : "-.--. ",
    ')' : "-.--.- ",
    '"' : ".-..-. ",
    '.' : ".-.-.- ",
    ',' : "--..-- ",
    '?' : "..--.. ",
    '/' : "-..-. ",
    '@' : ".--.-. ",
    '-' : "-....- ",
    '1' : ".---- ",
    '2' : "..--- ",
    '3' : "...-- ",
    '4' : "....- ",
    '5' : "..... ",
    '6' : "-.... ",
    '7' : "--... ",
    '8' : "---.. ",
    '9' : "----. ",
    '0' : "----- ",
    '\n': "//",
}

morse_code_dict = {
        '.- ': 'A', '-... ': 'B', '-.-. ': 'C', '-.. ': 'D', '. ': 'E',
        '..-. ': 'F', '--. ': 'G', '.... ': 'H', '.. ': 'I', '.--- ': 'J',
        '-.- ': 'K', '.-.. ': 'L', '-- ': 'M', '-. ': 'N', '--- ': 'O',
        '.--. ': 'P', '--.- ': 'Q', '.-. ': 'R', '... ': 'S', '- ': 'T',
        '..- ': 'U', '...- ': 'V', '.-- ': 'W', '-..- ': 'X', '-.-- ': 'Y',
        '--.. ': 'Z',
        '.---- ': '1', '..--- ': '2', '...-- ': '3', '....- ': '4', '..... ': '5',
        '-.... ': '6', '--... ': '7', '---.. ': '8', '----. ': '9', '----- ': '0',
        # '': ' ',
        '/': ' ',
            ".----. ":'\'',
    "-.--. ":'(',
     "-.--.- ":')',
     ".-..-. ": '"',
    ".-.-.- " : '.' ,
     "--..-- ": ',',
    "..--.. " : '?' ,
     "-..-. ": '/' ,
     ".--.-. ": '@',
    "-....- ": '-' ,
    }

def encode(s):
    m = ""
    for char in s:
        char = morse[char]
        m = m + char
    return m

def decode(code):

    words = code.split('/')  # Split the Morse code by spaces to get individual words
    decrypted_message = ''
    for word in words:
        letters = word.split(' ')  # Split each word by spaces to get individual letters in Morse code
        for letter in letters:
            decrypted_message += morse_code_dict[letter]  # Convert each Morse code letter to its corresponding character
        decrypted_message += ' '  # Add space between words
    return decrypted_message.strip()  # Remove leading/tra


def main() -> None:
    choice = input("Encode(E)\nDecode(D)\n")
    if choice.upper() =='E' :
        s = input("\nWhat is the string to be encoded?\n")
        s = s.upper()
        print(encode(s))
    if choice.upper() == 'D':
        s = input("What is the string to be decoded?\n(-Give space after writing a letter\n-Enter '/' after writing a word\n-Enter '//' for a new line)\n")
        print(decode(s))
