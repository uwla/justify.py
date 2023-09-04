#!/usr/bin/python3

def safe_input():
    try:
        return input()
    except EOFError:
        return None

def read_input():
    str = ''
    line = safe_input()
    while line != None:
        str += line + "\n"
        line = safe_input()
    return str

def justify(text, n=80):
    words = text.split()
    sentences = [
        {
            'length': 0,
            'words': [],
        }
    ]
    current_sentence_length = 0
    for word in words:
        word_length = len(word)
        if n < current_sentence_length + word_length + 1:
            current_sentence_length = word_length
            sentence = {
                'length': word_length,
                'words': [word],
            }
            sentences.append(sentence)
        else:
            sentence = sentences[-1]
            sentence['words'].append(word)
            if sentence['length'] == 0:
                word_length -= 1
            sentence['length'] += word_length + 1
            current_sentence_length += word_length + 1

    text = ''
    for sentence in sentences[:-1]:
        line = ''
        words = [w for w in sentence['words']]
        words.reverse()
        n_words = len(words)

        if n_words == 0:
            continue
        elif n_words == 1:
            total_extra_spaces = 0
            remaining_spaces = 0
            space_per_gap = 0
        else:
            total_extra_spaces = n - sentence['length']
            space_gaps = n_words - 1
            space_per_gap = total_extra_spaces//space_gaps
            remaining_spaces = total_extra_spaces - space_per_gap * space_gaps

        for word in words[:-1]:
            if remaining_spaces > 0:
                extra_spaces = space_per_gap + 1
                remaining_spaces -= 1
            else:
                extra_spaces = space_per_gap

            spaces = ' ' + ' ' * extra_spaces
            line = spaces + word + line
        line = words[-1] + line
        text += line + "\n"

    last_sentence = sentences[-1]
    text += ' '.join(last_sentence['words'])

    return text


text = read_input()
text_justified = justify(text)
print(text_justified)
