import random


li = []
i = 0


def random_list():
    val = [i for i in range(1, 11)]

    random.shuffle(val)

    li.append(val)


while i < 100:
    random_list()
    i += 1


"""
new_li = []
for li1 in li:
    if li1 not in new_li:
        new_li.append(li1)
print(new_li)


print(len(new_li))
"""

new_li = list(set(li))
print(len(new_li))