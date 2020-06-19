count = 0
iteration = 0
def count_th(word):
    if word == "":
        return count
    chars = list(word)
    if len(chars) > 0:
        if chars[0]+chars[1] == "th":
            chars.pop(0)
            if len(chars) != 0:
                count_th(chars)
        elif chars[0]+chars[1] != "th":
            chars.pop(0)
            count_th(chars)
    return count

try_this = "gadhfthlka"
chars = list(try_this)
length = len(chars)
print(length)
# count_th(try_this))
for i in range(len(chars)):
    print(chars[0])
    chars.pop(0)
print(chars)
    