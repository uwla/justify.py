#!/usr/bin/python3

from sys import argv
import re

# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------

def is_alphanumeric(c):
    return re.match('^[a-zA-Z0-9]$', c)

def is_blank(line):
    return line == '' or re.match('^[\s\t]+$', line)

def text2blocks(text):
    lines = text.splitlines()
    last_line = None
    blocks = []
    block = ''
    l = len(lines)
    for i in range(0, l):
        line = lines[i]
        # print(block)
        if is_blank(line):
            blocks.append(block)
            blocks.append(line)
            block = ''
        else:
            if block != '':
                block += '\n'
            block += line
            if i == l-1:
                blocks.append(block)
    return blocks

# ------------------------------------------------------------------------------

def detect_indentation(text):
    """Detect if consecutive lines have the same indentation level

    Args:
        text (string): string representing a text block

    Returns:
        string: the indentation
    """

    lines = text.split('\n')
    l = len(lines)
    if l == 0:
        raise Exception('No lines detected')

    first_line = lines[0]
    match = re.search('^[\s\t]+', first_line)

    # no indentation
    if match == None:
        return ''
    
    indentation = match.group()

    for i in range(1, l):
        line = lines[i]
        match = re.search('^[\s\t]+', line)
        if match == None:
            return ''
        current_line_indentation = match.group()
        if current_line_indentation != indentation:
            return ''

    return indentation

def detect_common_prefix(text):
    """Detect if consecutive lines have the same text at the beginning.
    Can be used to detect comments.

    Args:
        text (string): string representing a text block

    Returns:
        string: the indentation
    """

    lines = text.splitlines()
    l = len(lines)
    if l < 2:
        return ''

    pattern = ''
    i = 0
    while True:
        stop = False
        if len(lines[0]) <= i:
            break
        c = lines[0][i]
        if is_alphanumeric(c):
            break
        for line in lines[1:]:
            l = len(line)
            if (i >= l and c != ' ') or (i < l and line[i] != c):
                stop = True
                break
        if stop:
            break
        pattern += c
        i += 1

    return pattern

def remove_common_prefix(text, prefix):
    lines = text.splitlines()
    new_text = ''

    for line in lines:
        new_line =  line.replace(prefix, '')

        # HEURISTIC: if the prefix ends with space,
        # we consider removing the prefix without the last space.
        if new_line == line and prefix.endswith(' '):
            new_line =  line.replace(prefix[:-1], '')

        new_text += new_line + '\n'
    return new_text

def prepend_common_prefix(text, prefix):
    lines = text.splitlines()
    new_text = ''
    for line in lines:
        new_text += prefix + line + '\n'
    return new_text

# ------------------------------------------------------------------------------

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

def justify_blocks(text, n=80, depth=1):
    blocks = text2blocks(text)
    new_text = ''
    for block in blocks:
        if is_blank(block):
            new_text += '\n'
        else:
            prefix = detect_common_prefix(block)
            l = len(prefix)
            block = remove_common_prefix(block, prefix)
            if depth > 0 and l > 0:
                block = justify_blocks(block, n-l, depth-1)
            else:
                block = justify(block, n-l)
            block = prepend_common_prefix(block, prefix)
            new_text += block

    # for some reason, the algorithm adds an extra new line. So, remove it.
    new_text = new_text[:-1]

    return new_text

# ------------------------------------------------------------------------------
# MAIN

# default line width
w = 80

# dumb args parser
if len(argv) == 3:
    if argv[1] == "-w":
        w = int(argv[2])

text = read_input()
text_justified = justify_blocks(text, w)
print(text_justified)
