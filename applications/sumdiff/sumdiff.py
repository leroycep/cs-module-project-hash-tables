"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import itertools

#q = set(range(1, 10))
#q = set(range(1, 200))
q = set([1, 3, 4, 7, 12])


def f(x):
    return x * 4 + 6

for a in q:
    for b in q:
        for c in q:
            for d in q:
                if (f(a) + f(b)) == (f(c) - f(d)):
                    print(f"f({a}) + f({b}) == f({c}) - f({d})    {f(a)} + {f(b)} == {f(c)} - {f(d)}")
