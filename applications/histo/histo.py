import sys

if len(sys.argv) != 2:
    print("wrong number of arguments")

with open(sys.argv[1]) as f:
    contents = f.read()


def normalize_word(word):
    ignored_characters = "\":;,.-+=/\|[]{}()*^&"
    s = ''
    for c in word:
        if c not in ignored_characters:
            s = s + c
    return s.lower()


word_counts = {}
words = contents.split()
longest_word_length = 0
for word in words:
    pretty_word = normalize_word(word)
    if pretty_word == "":
        continue

    # add the pretty_word occurance to the counts
    if pretty_word in word_counts:
        word_counts[pretty_word] += 1
    else:
        word_counts[pretty_word] = 1

    # check if the pretty_word is longer than the previous longest word
    if len(pretty_word) > longest_word_length:
        longest_word_length = len(pretty_word)

count_list = [(word_counts[word], word) for word in word_counts]
count_list.sort(reverse=True)

for (count, word) in count_list:
    print(word.ljust(longest_word_length), end="  ")
    print("#" * count)
