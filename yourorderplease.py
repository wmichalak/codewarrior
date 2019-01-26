import re

def order(sentence):
    if sentence == "":
        return ""
    numbers = list(map(int, re.findall('\d+', sentence)))
    s = sentence.split(" ")
    new_sentence = [None] * len(s)
    for i, idx in enumerate(numbers):
        new_sentence[idx - 1] = s[i]

    return " ".join(new_sentence)