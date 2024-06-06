# original less refined approach takes longer
import json
from collections import Counter

with open("./data.txt", "r", encoding="utf-8") as f:
    text = f.read()


print(f"number of characters in the dataset:{len(text)}")
chars = sorted(list(set(text)))
print("".join(chars))
text = list(text)


def combine_subsequence(chars, subsequence):
    i = 0
    while i < len(chars) - 1:
        if chars[i : i + len(subsequence)] == subsequence:
            chars[i] += chars.pop(i + 1)
        else:
            i += 1
    return chars


def BPE(text, vocabsize):
    lst = []
    while len(text) > vocabsize:
        for i in range(len(text) - 1):
            lst.append("".join(text[i : i + 2]))

        lst = Counter(lst)
        freqtok = lst.most_common(len(list(lst.keys())) // 10)
        keys = [item[0] for item in freqtok]
        lst = list(lst.keys())
        for key in keys:
            print(key)
            text = combine_subsequence(text, ["".join(lst[:-1]), "".join(lst[-1])])

        print(len(text))
        text = Counter(text)
        print(max(list(text.keys())))

    return lst


text = Counter(text.extend(BPE(text, 1000)))
with open("output.json", "w") as outfile:
    json.dump(chars, outfile, indent=2)
