import random
import string
import math

# random_pass = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(12)])
def genChars(type, count):
    if type == "string":
        return [random.choice(string.ascii_letters) for n in range(count)]
    elif type == "number":
        return [random.choice(string.digits) for n in range(count)]
    else:
        return [random.choice(string.punctuation) for n in range(count)]


def getCounts(opCount, length):
    cSum = sum(range(opCount)) + 3
    counts = []
    for i in range(opCount):
        count = ((i+1)*length) / cSum
        counts.append(count)
    return counts


def genPassword():
    try:
        charCount = getCounts(3,16)
        characters = genChars("string", charCount[random.randint(0,2)])
        numbers = genChars("number", charCount[random.randint(0,2)])
        symbols = genChars("symbol", charCount[random.randint(0,2)])
        return "".join(characters+numbers+symbols)
    except Exception as err:
        print("error: {}".format(err))

print(genPassword())