import re

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

def trim_lines(text):
    """Trim empty lines at both ends of a text
        Args:
            text_block (string): string representing a text block
        Returns:
            string: the indentation
    """
    lines = text.split('\n')

    l = len(lines)
    if l == 0:
        raise Exception('No lines')

    if lines[0] == '':
        lines = lines[1:]

    l = len(lines) 
    if l > 0 and lines[-1] == '':
        lines = lines[0:(l-1)]
    
    return '\n'.join(lines)

sometext = """
			opa ganga
			heehe
			vish ops
			new
"""

print(len(detect_indentation(trim_lines(sometext))))