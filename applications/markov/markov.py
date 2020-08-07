import re
import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here


following_words = {}


wordsiter = iter(words.split())
prev_word = next(wordsiter)
for current_word in wordsiter:
    if prev_word in following_words:
        following_words[prev_word].append(current_word)
    else:
        following_words[prev_word] = [current_word]
    prev_word = current_word


def is_stop_word(word):
    return word.endswith(".") or word.endswith("?") or word.endswith("!") or word.endswith('."') or word.endswith('?"') or word.endswith('!"')


def print_chain_of_words(following_words):
    word = random.choice(list(following_words.keys()))
    while True:
        print(word, end=" ")
        if is_stop_word(word):
            break
        word = random.choice(following_words[word])
    print()


for i in range(5):
    print_chain_of_words(following_words)
    print()
