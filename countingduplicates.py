def duplicate_count(text):
    text = text.lower()
    dups = 0
    dup_char = []
    for char in text:
        if text.count(char) > 1 and char not in dup_char:
            dup_char.append(char)
            dups += 1
    return dups
