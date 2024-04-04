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
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
        '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
        '': ' '
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


choice = input("Encode(E)\nDecode(D)\n")
if choice.upper() =='E' :
    s = input("\nWhat is the string to be encoded?\n")
    s = s.upper()
    print(encode(s))
if choice.upper() == 'D':
    s = input("What is the string to be decoded?\n(-Give space after writing a letter\n-Enter '/' after writing a word\n-Enter '//' for a new line)\n")
    print(decode(s))

'''
/This is a long writing, so... take your time i guess/. So, you have deciphered the code. I didn't have doubt to be honest. Anyway, How are you? You have become tremendously busy since beginning of your college. Your achievements, atleast the ones that I am aware of, are inspirational to me. Hope Vicky is doing well. Coming to the reason I am writing this in this mail thread is because... well I will get to it in a while. Since I cannot expect to have a concurrent conversation going on using a SMTP-induced application, I will continue to yap about myself. I am nearing the end of my 2nd year. In the beginning of my college life, I had the choice of either sitting in my room and laze around or go outside and dedicate myself to various different activites, learn new things, make new relations. All of my friends are so unique. One who is sitting right beside me now, is such an amazing computer nerd. I thoroughly enjoy spending time with him, as it's always an intriguing and energetic exchange. There is another fellow who is highly lazy. Like, 9 out of 10 times, if you ask him, let's do something, you can expect a swift no, for an answer. However, he was my teammate in a hackathon we competed in recently. We won the 2nd prize, and I would dedicate a huge thanks to his dedication. I mean, due to this we even got an internship offer... it's just like... wow. There's another kid, a highly gifted musician, instrumentalist and singer. He and I have the most mutual friend groups. Then, there is my current roommate. He and I have the most understanding here. He is perhaps the most extroverted person in the college after me. Also, there is this girl, whom I call my daughter. It did start as a joke, but now I have fatherly instincts towards her (I know, weird. But... idk). She is highly smart and diligent. Another girl, a total girl boss, to be honst, an academic bull and a very passionate person and an amazing dancer. For me she is an invaluable friend. Like when I fainted and fell down and got the cut on my head, she became frantic. The amount of messages I recieved from her stating I should be more careful is overwhelming to say the least. And I haven't even gotten to my senior friends, who all are highly skilled and very talented in their own ways. They provide such a ambitious template for me to follow. My junior friends, who even though are still learning the ropes, are proving themselves in many ways. If I go on telling about everyone, you would be reading the biodata of half of IIIT Sri City. I mean, I haven't even talked about some of the people who I have very recently become more close to. But... I don't know if you are even interested as you used to be before. So, I will save myself the trouble. You remember, how I used to tell you that I always wanted to be a good leader. I feel I am on that path right now. But, believe me, it's exhausting. I mean... I am one of the two marketing heads of the college, was in the organiser team for the annual fest this time around, literally founded and work on the college newsletter. The work I had to do, am doing... it takes so much effort, with almost no thanks in proportion. Yet, I do it without complaining. Because, I know, if I don't... the chances of somebody else doing it properly, is low. I want to spend more time with my friends Vaishu. More time doing shit that does not matter. It feels like it's been a long time since I have taken a break, even though I technically went and came back from home last week itself. The stress is overbearing. And, I am seriously not happy with my academics. Like the effort I put in, and the returns I get... like... emo ra... naaku em cheyalo teliyatledu. Does not matter, if I attend all classes, read the textbook, watch every video related to the topics. No matter if I write the entire paper correctly, I can never seem to be getting the marks I actually deserve. This has been the case for my entire college life now. I no longer know what I am doing wrong. Sometimes, I get suicidal thoughts, but then I remember, there are people who depend on me, people are looking up to me, looking out for me. I just think what shock and disappointment they would have to go through if I advance, and I let the thoughts bury themselves. The other day, I went out with my friends, and one of them told she broke up with her boyfriend, and continued to give her reason. It for some reason, felt very similar to your reason. This led me to go to the mail and review it once. There, I once again go through the agonizing period of time in my life. I see some of your responses, of how we will talk after the exams, it's not entirely a breakup, etc. Of all of that, I see one thing, that I feel I didn't let you down on, and that is you wanting me to be strong. To face an adversity, without faltering. I smile to myself, and say "You can tick that off now Vaishu". I have a hunch that you have a boyfriend now. And writing all of this seems like such a bad idea if my hunch is right. But, even after two years, the only person I am still excited to talk to, to chat with, still remains the same. Everyday, with the crushing pain of my responsibilities growing, I just wish, I had my girlfriend, just to have someone to talk to, whom I am sure that I don't have to worry if I am making her worry much, or that I am wasting her time. Right now, I am at that point of life, that all of these are seeming toxic traits in me. Believe me, every day, I try to dedicate myself to make the world a better place in some way I can. Yet, in trying to do this, I feel like I lose another little fragment of myself. I feel like I want to have you back, but with each passing day, my confidence diminishes and I convince myself to try on someone new. But, I never feel like I can spend my time with this person with anyone else. I know, I can just date them and leave, have fucking sex and drinks and all shit. But, doing that would mean I am violating myself, becoming somebody I am not. I don't know what will be of this mail, don't even know if you will read it. I don't know what to expect. Even then, I know, that the only person I want to speak to, is still you. I know, this is not what you expected, maybe not wanted too. And for that I apologize. I will try to forget you, as I have been since a very long time now. Thank you for making the best memories of my life.
'''