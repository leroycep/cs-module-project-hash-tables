"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
#q = set(range(1, 10))
q = set(range(1, 200))
#q = set([1, 3, 4, 7, 12])


def f(x):
    return x * 4 + 6

# Loop through all possible combinations of a and b.
# I tried to do a clever thing where, since a + b == b + a, I would
# only try out all of the (a, b) combinations, and then account for it later.
# The problem with that method was that I would have to generate the reversed
# pairs at the end, and then make sure that when a == b it didn't count for
# two matches. I decided to keep it simple, and this method is so much faster
# than the brute force that the micro-optimization I though of wouldn't matter.
sums = {}
for a in q:
    for b in q:
        sum = f(a) + f(b)
        if sum in sums:
            sums[sum].append((a, b))
        else:
            sums[sum] = [(a, b)]

diffs = {}
for c in q:
    for d in q:
        diff = f(c) - f(d)
        if diff in diffs:
            diffs[diff].append((c, d))
        else:
            diffs[diff] = [(c, d)]

matches = 0

for sum in sums:
    if sum in diffs:
        matches += len(sums[sum]) * len(diffs[sum])
        # Uncomment if you want your terminal to be filled with garbage:
        # for (a, b) in sums[sum]:
        #     for (c, d) in diffs[sum]:
        #         print(f"f({a}) + f({b}) = f({c}) - f({d})    {f(a)} + {f(b)} = {f(c)} - {f(d)}")

print(f"\n{matches} matching combinations")
