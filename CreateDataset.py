from datasets import load_dataset

dataset = load_dataset("wikitext", name="wikitext-2-raw-v1", split="train")
text = dataset["text"]

def dump_list_to_file(lst, filename):
    with open(filename, 'w') as f:
        for element in lst:
            f.write(str(element) + '\n')

dump_list_to_file(text, "data.txt")
