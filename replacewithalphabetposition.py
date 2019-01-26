def alphabet_position(text):
    alpha_dict = {j:i for i,j in enumerate('abcdefghijklmnopqrstuvwxyz')}
    output = []
    for char in text.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz':
            output.append(str(alpha_dict[char]+1))
    return " ".join(output)