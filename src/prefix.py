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

    pattern = ''
    i = 0
    while True:
        stop = False
        if len(lines[0]) <= i:
            break
        c = lines[0][i]
        for line in lines[1:]:
            if len(line) <= i or line[i] != c:
                stop = True
                break
        if stop:
            break
        pattern += c
        i += 1

    return pattern

a = """
# cupiditate laborum.Dicta similique quaerat totam ipsum delectus et. Sequi
# consequatur aliquam et culpa omnis et assumenda. Dignissimos ad quo totam
# excepturi.
"""
b = """
        // Unde consectetur sunt eos corrupti laboriosam quam omnis. Quae sunt aut
        // assumenda. Aliquam molestias voluptate omnis rerum. Totam qui saepe aut sed
        // cupiditate laborum.Dicta similique quaerat totam ipsum delectus et. Sequi
        // consequatur aliquam et culpa omnis et assumenda. Dignissimos ad quo totam
        // excepturi.
"""

print(detect_common_prefix(trim_lines(a)))
print(detect_common_prefix(trim_lines(b)))