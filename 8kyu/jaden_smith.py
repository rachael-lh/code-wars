import string

jaden = "How can mirrors be real if our eyes aren't real"


def to_jaden_case(words):
    return string.capwords(words)


print(to_jaden_case(jaden))


# jaden_message = "How can mirrors be real if our eyes aren't real"


# def to_jaden_case(jadens_message):
#     jaden_words = [word for word in jadens_message.split(" ")]
#     result = ""
#     i = 1
#     for jaden_word in jaden_words:
#         if jaden_word != "":
#             result += jaden_word[0].upper() + jaden_word[1:].lower()
#         if len(jaden_words) != i:
#             result += " "
#             i += 1

#     return result


# print(to_jaden_case(jaden_message))
