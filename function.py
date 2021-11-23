from translate import to_cyrillic, to_latin
from num_text import num_text
def latin_text(number):
    text = ''
    i = 0
    for num_order in range(len(number), 0, -1):
        if len(number) >= 4 and number[-4] == '0' and num_order == 4:
            text += (num_text[str(num_order)][number[i]] + 'ming ')
        else:
            text += (num_text[str(num_order)][number[i]]) +' '
        i += 1
    return text

def translit(message):
    return to_cyrillic(message)