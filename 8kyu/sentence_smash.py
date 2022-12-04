words = ["hello", "world", "this", "is", "great"]


def smash(words):
    sentence = ""
    i = 1
    for a_word in words:
        sentence += a_word
        if len(words) != i:
            sentence += " "
            i += 1
    return sentence


print(smash(words))

# words = ["hello", "world", "this", "is", "great"]

# solution 2:
def smash(words):
    res = " ".join(words)
    return res


# print(smash(words))
