import re

word_re = re.compile(r"[a-z]+")


def no_dups(s):
    global word_re

    seen_words = set({})
    new_string = ""

    for match in word_re.finditer(s.lower()):
        word = match.group()
        if word not in seen_words:
            seen_words.add(word)
            if new_string == "":
                new_string = word
            else:
                new_string = new_string + " " + word

    return new_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
