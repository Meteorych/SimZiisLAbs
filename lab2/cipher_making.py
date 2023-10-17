import itertools
import random
import string
import time
from itertools import cycle

alphabet = list(string.ascii_lowercase)


def generate_keyword():
    keyword = ""
    for i in random.choices(alphabet, k=random.randint(5, 12)):
        keyword += i
    print(f"Keyword: {keyword}")
    return keyword


def making_cipher(keyword: str):
    begin_word = input("Input word that you want to cipher: ")
    f = lambda arg: alphabet[(alphabet.index(arg[0]) + alphabet.index(arg[1]) % 26) % 26]
    cipher_word = ''.join(map(f, zip(begin_word, cycle(keyword))))
    print(f"\nCipher word: {cipher_word}")
    decode_cipher(cipher_word, begin_word)


def decode_cipher(cipher_word: str, begin_word: str):
    start = time.time()
    decoded_word = ""
    for length in range(5, 12):
        for keyword in itertools.product(alphabet, repeat=length):
            f = lambda arg: alphabet[alphabet.index(arg[0]) - alphabet.index(arg[1]) % 26]
            decoded_word = ''.join(map(f, zip(cipher_word, cycle(keyword))))
            if decoded_word == begin_word:
                break
        if decoded_word != begin_word:
            continue
        else:
            break
    print(f"\nDecoded word: {decoded_word}")
    end = time.time()
    print(end - start)


