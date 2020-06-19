'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0
iteration = 0
def count_th(word):
    chars = list(word)
    print("preprint: ", chars)
    if len(word) > 0:
        if chars[0] + chars[1] == "th":
            print("string match")
            chars.pop()
            if len(chars) != 0:
                count_th(chars)
        elif chars[0] + chars[1] != "th":
            chars.pop(0)
            count_th(chars)
    return count