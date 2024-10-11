import string
import random

def encode(normal_words):
    # Converts your code to secret code
    if (len(normal_words)<3):
        print(normal_words[::-1])
    elif (len(normal_words)>3):
        letter = normal_words[1:]+normal_words[0]
        word_end = "".join(random.choices(string.ascii_lowercase, k=3))
        word_begin = "".join(random.choices(string.ascii_lowercase, k=3))
        secret_code = word_begin + letter + word_end
        print(f"Your secret code is:",secret_code)
    
def decode(Sec_Code):
    # Converts your secret code to code
    if (len(Sec_Code)<3):
        print(Sec_Code[::-1])
    elif (len(Sec_Code)>3):
        word = Sec_Code[3:-3]
        letter = word[-1]+word[:4]
        print(f"Your code is:",letter)

print("Hey! Do you want to encode or decode?")
choice = int(input("1 for encode and 2 for decode: "))

match choice:
    case 1:
        normal_words = input("Encode Word: ")
        encode(normal_words)
    case 2:
        Sec_Code = input("Decode Word: ")
        decode(Sec_Code)