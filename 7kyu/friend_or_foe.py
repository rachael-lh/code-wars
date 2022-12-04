# friends = ["Ryan", "Kieran", "Jason", "Alex"]

# solution 1:
def friend(friend):
    amigos = []
    for name in friend:
        if len(name) == 4:
            amigos.append(name)

    return amigos


# print(friend(friends))

# solution 2:
def friend(x):
    return [f for f in x if len(f) == 4]
