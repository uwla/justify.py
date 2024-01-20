#!/usr/bin/python3
import re

# ------------------------------------------------------------------------------
# INPUT HELPERS

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
# HELPERS

def is_blank(line):
    return line == '' or re.match('^[\\s\t]+$', line) != None

REGEX_BULLET = '\\d+[\\.\\)]|[\\*-]|\\\\item|\\[\\d+\\]'
REGEX_LIST_ITEM = f"^({REGEX_BULLET}) "
REGEX_LIST_ITEM_INDENTED = f"^[\\s\t]+({REGEX_BULLET}) "

def is_start_of_list_item(line):
    return re.match(REGEX_LIST_ITEM, line) != None
    # return re.match('^(\\d+[\\.\\)]|[\\*-]|\\\\item|\\[\\d+\\]|•|·) ', line) != None

def indented_start_of_list_item(line):
    return re.match(REGEX_LIST_ITEM_INDENTED, line) != None

def is_latex_command(line):
    return re.match('^\\\\[a-z]+(\\[.*?\\])?{.*?}$', line) != None

def is_line_title(line):
    return re.match('^#+ .+', line) != None or (re.match('^(\\w\\s?)+', line) != None and re.match('[a-z]', line) == None)

def text2blocks(text):
    """Split a text into blocks. Each  block  represents  consecutive  lines  or
    empty lines.

    Args:
        text (string): text to be splitted

    Returns:
        list<string>: a list of blocks, which are strings.
    """
    lines = text.splitlines()
    last_line = None
    blocks = []
    block = ''
    l = len(lines)

    last_indentation = ''

    for i in range(0, l):
        line = lines[i]
        if is_blank(line):
            if block != '':
                blocks.append(block)
            blocks.append(line)
            block = ''
        elif is_start_of_list_item(line):
            if block != '':
                blocks.append(block)
            block = line
        # elif is_line_title(line):
        #     if block != '':
        #         blocks.append(block)
        #         block = ''
        #     blocks.append(line)
        elif is_latex_command(line):
            if block != '':
                blocks.append(block)
            blocks.append(line)
            block = ''
        else:
            ## trying to detect indentation switch
            # m = re.match('^[\s\t]+', line)
            # if m != None and not indented_start_of_list_item(line) and not is_blank(block):
            #     indentation = m.group()
            #     if indentation != last_indentation:
            #         last_indentation = indentation
            #         blocks.append(block)
            #         block = ''

            if block != '':
                block += '\n'
            block += line

        # We are in the last line and have a non-empty block we need to add it.
        # If it is a blank block, it was already added.
        if not is_blank(block) and i == l-1:
            blocks.append(block)

    return blocks

# ------------------------------------------------------------------------------
# PREFIX AND INDENTATION HELPERS

def detect_indentation(text):
    """Detect if consecutive lines have the same indentation level

    Args:
        text (string): string representing a text block

    Returns:
        string: the indentation itself
    """

    lines = text.splitlines()
    l = len(lines)
    if l == 0:
        raise Exception('No lines detected')

    first_line = lines[0]
    match = re.search('^[\\s\t]+', first_line)

    # no indentation
    if match == None:
        return ''
    
    indentation = match.group()

    for line in lines[1:]:
        if not line.startswith(indentation):
            return ''

    return indentation

def detect_multiline_prefix(text):
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
        for line in lines[1:]:
            l = len(line)
            if (i >= l or line[i] != c):
                stop = True
                break
        if stop:
            break
        pattern += c
        i += 1

    # Some list item bullets such as *, -, \item, are  not  treated  like  prefixes
    # because such prefixes only apply  to  the  first  line,  not  to  all  lines.
    # Therefore, if pattern matches a list item, it is not a prefix.
    if indented_start_of_list_item(pattern):
        return ''

    # remove alpha numeric characters from pattern
    pattern = re.sub(r'\w.*', '', pattern)

    # return the final pattern, which may be empty
    return pattern

def remove_multiline_prefix(text, prefix):
    """Removes a prefix from every line of the given text.

    Args:
        text (string): prefixed text
        prefix (string): prefix

    Returns:
        string: text without prefix
    """
    lines = text.splitlines()
    new_text = ''
    for line in lines[:-1]:
        new_line =  line.replace(prefix, '', 1)
        new_text += new_line + '\n'
    new_text += lines[-1].replace(prefix, '', 1) + '\n'
    return new_text

def prepend_multiline_prefix(text, prefix):
    """Prepend a prefix to all lines of the given text.

    Args:
        text (string): unprefixed text
        prefix (string): prefix.

    Returns:
        string: text with prefix
    """
    lines = text.splitlines()
    new_text = ''
    for line in lines[:-1]:
        new_text += prefix + line + '\n'
    new_text += prefix + lines[-1] + '\n'
    return new_text

# ------------------------------------------------------------------------------
# JUSTIFY LOGIC

def justify_block(text, n=80):
    """Justify a single block of text that has no empty lines.

    Args:
        text (string): Text to be justified
        n (int): line Width. Defaults to 80.

    Returns:
        string: justified text block.
    """
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


def justify_list_item(text, n):
    """Justify a list item text, indenting its line accordingly.

    Args:
        text (string): text representing a list item block
        n (int): line width

    Returns:
        string: justified list item text
    """
    match = re.match(REGEX_LIST_ITEM, text)
    bullet = match[0]
    l = len(bullet)
    indentation = ' ' * l
    new_text = justify_block(text.replace(bullet, '', 1), n-l)
    new_text = prepend_multiline_prefix(new_text, indentation)
    new_text = new_text.replace(indentation, bullet, 1)
    return new_text

def justify(text, n=80, depth=2):
    """Justify-align the given text

    Args:
        text (string): Text to be justified.
        n (int): Line width. Defaults to 80.
        depth (int): How deep to justify the text's inner blocks. Defaults to 2.

    Returns:
        string: justified text
    """
    indentation = detect_indentation(text)
    if indentation != '':
        blocks = text2blocks(remove_multiline_prefix(text, indentation))
    else:
        blocks = text2blocks(text)
    n -= len(indentation)
    new_text = ''
    for block in blocks:
        if is_blank(block):
            new_text += '\n'
        elif is_start_of_list_item(block):
            block = justify_list_item(block, n)
            block = re.sub('\n', '\n' + indentation, block)
            new_text += indentation + block
        else:
            prefix = detect_multiline_prefix(block)
            if prefix == '':
                prefix = detect_indentation(block)
            l = len(prefix)
            block = remove_multiline_prefix(block, prefix)
            if depth > 0 and l > 0:
                block = justify(block, n-l, depth-1)
            else:
                block = justify_block(block, n-l)
            block = prepend_multiline_prefix(block, indentation + prefix)
            new_text += block

    return new_text

# ------------------------------------------------------------------------------
# MAIN

if __name__ == "__main__":
    # default line width
    w = 80

    # dumb args parser
    from sys import argv
    if len(argv) == 3:
        if argv[1] == "-w":
            w = int(argv[2])

    text = read_input()
    text_justified = justify(text, w)
    print(text_justified, end='')

