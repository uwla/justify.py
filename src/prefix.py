from indentation import trim_lines

def detect_common_prefix(text):
    """Detect if consecutive lines have the same text at the beginning.
    Can be used to detect comments.

    Args:
        text (string): string representing a text block

    Returns:
        string: the indentation
    """

    lines = text.split('\n')
    l = len(lines)
    if l < 2:
        raise Exception('No enough lines')

    a = lines[0]
    b = lines[1] 
    la = len(a)
    lb = len(b)
    i = 0
    pattern = ''
    while i < la and i < lb:
        if a[i] == b[i]:
            pattern += a[i]
        else:
            break
        i += 1

    if pattern == '':
        return pattern
    
    for i in range(2, l):
        line = lines[i]
        if not line.startswith(pattern):
            return ''

    return pattern

a = """
# cupiditate laborum.Dicta similique quaerat totam ipsum delectus et. Sequi
# sonsequatur aliquam et culpa omnis et assumenda. Dignissimos ad quo totam
# excepturi.
"""
b = """
        // Unde consectetur sunt eos corrupti laboriosam quam omnis. Quae sunt aut
        // assumenda. Aliquam molestias voluptate omnis rerum. Totam qui saepe aut sed
        // cupiditate laborum.Dicta similique quaerat totam ipsum delectus et. Sequi
        // consequatur aliquam et culpa omnis et assumenda. Dignissimos ad quo totam
        // excepturi.
"""

print(detect_common_start(trim_lines(a)))
print(detect_common_start(trim_lines(b)))