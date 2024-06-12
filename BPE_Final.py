import json
from collections import Counter, defaultdict

with open("./data.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(f"Number of characters in the dataset: {len(text)}")

chars = sorted(list(set(text)))
print("".join(chars))

def get_pairs(text):
    pair = []
    for i in range(len(text) - 1):
        pair.append((text[i], text[i + 1]))
    pairs = Counter(pair)
    return pairs


def merge_pair(text, pairs):
    merged_text = []
    i = 0
    merged_pairs = [pair[0] for pair in pairs]  # Extract the pairs to merge
    while i < len(text):
        if i < len(text) - 1 and (text[i], text[i + 1]) in merged_pairs:
            merged_text.append(text[i] + text[i + 1])
            i += 2
        else:
            merged_text.append(text[i])
            i += 1

    return merged_text

def BPE(text, vocab_size):
    vocab = Counter(text)
    print(len(vocab))
    while len(vocab) < vocab_size:
        pairs = get_pairs(text)
        if not pairs:
            break
        most_common_pairs = pairs.most_common(500)
        print(most_common_pairs)
        text = merge_pair(text, most_common_pairs)
        vocab = Counter(text)
        print(f"Most common pair: {most_common_pairs}")
        print(f"Vocabulary size: {len(vocab)}")
    return vocab


vocab_size = 50000
final_vocab = BPE(text, vocab_size)
final_vocab = sorted(list(final_vocab.keys()))
final_vocab = {key: index for index,key in enumerate(final_vocab)}
print(final_vocab)

with open("output.json", "w", encoding="utf-8") as outfile:
    json.dump(final_vocab, outfile, indent=2)
