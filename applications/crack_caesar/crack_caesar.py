# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

import sys

if len(sys.argv) != 2:
    print("wrong number of arguments")

with open(sys.argv[1]) as f:
    contents = f.read().lower()

letter_counts = {}
total_letters = 0
for letter in contents:
    if letter >= 'a' and letter <= 'z':
        total_letters += 1
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

count_list = [(letter_counts[letter], letter) for letter in letter_counts]
count_list.sort(reverse=True)

for (count, letter) in count_list:
    frequency = count / total_letters * 100
    print(f"{letter}  {frequency}")

# The most frequent letter should be e
cipher = {}
cipher[count_list[0][1]] = 'e'
cipher[count_list[1][1]] = 't'
cipher[count_list[2][1]] = 'a'
cipher[count_list[3][1]] = 'o'
cipher[count_list[4][1]] = 'h'
cipher[count_list[5][1]] = 'n'
cipher[count_list[6][1]] = 'r'
cipher[count_list[7][1]] = 'i'
cipher[count_list[8][1]] = 's'
cipher[count_list[9][1]] = 'd'
cipher[count_list[10][1]] = 'l'
cipher[count_list[11][1]] = 'w'
cipher[count_list[12][1]] = 'u'
cipher[count_list[13][1]] = 'g'
cipher[count_list[14][1]] = 'f'
cipher[count_list[15][1]] = 'b'
cipher[count_list[16][1]] = 'm'
cipher[count_list[17][1]] = 'y'
cipher[count_list[18][1]] = 'c'
cipher[count_list[19][1]] = 'p'
cipher[count_list[20][1]] = 'k'
cipher[count_list[21][1]] = 'v'
cipher[count_list[22][1]] = 'q'
cipher[count_list[23][1]] = 'j'
cipher[count_list[24][1]] = 'x'
cipher[count_list[25][1]] = 'z'

for letter in contents:
    if letter >= 'a' and letter <= 'z':
        print(cipher[letter], end="")
    else:
        print(letter, end="")

