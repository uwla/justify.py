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