import re


word_re = re.compile(r"[a-z']+")

def word_count(s):
    global word_re

    word_counts = {}
    for match in word_re.finditer(s.lower()):
        word = match.group()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
