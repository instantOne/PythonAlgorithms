import re

input_text = input().strip()
#first_year(not Exactly)
def remove_e(match):
    word = match.group(0)
    if len(word) == 1 and word == 'e':
        return word
    else:
        return word[:-1]

input_text = re.sub(r'\b(?:a|an|the)\b', '', input_text, flags=re.IGNORECASE)
input_text = re.sub(r'ci', "si", input_text)
input_text = re.sub(r'Ci', "Si", input_text)
input_text = re.sub(r'ce', "se", input_text)
input_text = re.sub(r'Ce', "Se", input_text)
input_text = re.sub(r'ck', "k", input_text)
input_text = re.sub(r'Ck', "K", input_text)
input_text = re.sub(r'c', "k", input_text)
input_text = re.sub(r'C', "K", input_text)

#second_year
input_text = re.sub(r'Ee', "I", input_text)
input_text = re.sub(r'ee', "i", input_text)

input_text = re.sub(r'Oo', "U", input_text)
input_text = re.sub(r'oo', "u", input_text)

input_text = re.sub(r'([a-zA-Z])\1+', r'\1', input_text, flags=re.IGNORECASE)
input_text = re.sub(r'\b\w*e\b', remove_e, input_text)
input_text = re.sub(r'^\s', '', input_text)
input_text = re.sub(r'\s$', '', input_text)
input_text = re.sub(r'[\s]+', r' ', input_text, flags=re.IGNORECASE)



print(input_text)
