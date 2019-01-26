def duplicate_encode(word):
    parens = ''
    word = word.lower()
    for i, p in enumerate(word):
        if p in (word[0:i] + word[i+1::]):
            parens += ')'
        else:
            parens += '('
    return parens