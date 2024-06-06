import json
from collections import Counter, defaultdict

# Read the input text file
with open("./data.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(f"Number of characters in the dataset: {len(text)}")

# Create a sorted list of unique characters
chars = sorted(list(set(text)))
print("".join(chars))

# Convert text to a list of characters
text = list(text)
text


# Function to get pairs of consecutive characters
def get_pairs(text):
    pairs = defaultdict(int)
    for i in range(len(text) - 1):
        pair = (text[i], text[i + 1])
        pairs[pair] += 1
    return pairs


def merge_pair(text, pair):
    merged_text = []
    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i] == pair[0] and text[i + 1] == pair[1]:
            merged_text.append(text[i] + text[i + 1])
            i += 2
        else:
            merged_text.append(text[i])
            i += 1
    return merged_text


lst = [12, 4, 3, 12]
lst = Counter(lst)
len(lst)


# Function to perform Byte Pair Encoding (BPE)
def BPE(text, vocab_size):
    vocab = Counter(text)
    print(len(vocab))
    while len(vocab) < vocab_size:
        pairs = get_pairs(text)
        if not pairs:
            break
        most_common_pair = max(pairs, key=pairs.get)
        text = merge_pair(text, most_common_pair)
        vocab = Counter(text)
        print(f"Most common pair: {most_common_pair}")
        print(f"Vocabulary size: {len(vocab)}")
    return vocab


# and 20000
# highest frequency


# Perform BPE on the text
vocab_size = 1000
final_vocab = BPE(text, vocab_size)

# Save the vocabulary to a JSON file
with open("output.json", "w", encoding="utf-8") as outfile:
    json.dump(final_vocab, outfile, indent=2)

# Print the final vocabulary
print(f"Final vocabulary: {sorted(final_vocab.keys())}")
