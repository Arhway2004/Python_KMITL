# 1_1
def textese(s):
    abbreviations = {
        "be": "b",
        "because": "cuz",
        "see": "c",
        "the": "da",
        "okay": "ok",
        "are": "r",
        "you": "u",
        "without": "w/o",
        "why": "y",
        "see you": "cu",
        "ate": "8",
        "great": "gr8",
        "mate": "m8",
        "wait": "W8",
        "later": "I8r",
        "tomorrow": "2mro",
        "for": "4",
        "before": "b4",
        "once": "1ce",
        "and": "&",
        "Your": "ur",
        "You're": "ur",
        "As far as I know": "afaik",
        "As soon as possible": "ASAP",
        "At the moment": "atm",
        "Be right back": "brb",
        "By the way": "btw",
        "For your Information": "FYI",
        "In my humble opinion": "imho",
        "In my opinion": "imo",
        "Laughing out loud": "lol",
        "Oh my god": "omg",
        "Rolling on the floor laughing": "rofl",
        "Talk to you later": "ttyl"
    }
    words = s.split()
    abbreviated_words = [abbreviations.get(word, word) for word in words]
    abbreviated_message = " ".join(abbreviated_words)
    return abbreviated_message

message = "You're great ."
result = textese(message)
print(result)

# 1_2
def untextese(s):
    abbreviations = {
        "b": "be",
        "cuz": "because",
        "c": "see",
        "da": "the",
        "ok": "okay",
        "r": "are",
        "u": "you",
        "w/o": "without",
        "y": "why",
        "cu": "see you",
        "8": "ate",
        "gr8": "great",
        "m8": "mate",
        "W8": "wait",
        "I8r": "later",
        "2mro": "tomorrow",
        "4": "for",
        "b4": "before",
        "1ce": "once",
        "&": "and",
        "ur": "Your",
        "ur": "You're",
        "afaik": "As far as I know",
        "ASAP": "As soon as possible",
        "atm": "At the moment",
        "brb": "Be right back",
        "btw": "By the way",
        "FYI": "For your Information",
        "imho": "In my humble opinion",
        "imo": "In my opinion",
        "lol": "Laughing out loud",
        "omg": "Oh my god",
        "rofl": "Rolling on the floor laughing",
        "ttyl": "Talk to you later"
    }

    words = s.split()
    full_words = [abbreviations.get(word, word) for word in words]
    plain_message = " ".join(full_words)
    return plain_message

abbreviated_message = "u r gr8 ."
result = untextese(abbreviated_message)
print(result)

# 2
def composite(dict1, dict2):
    result = {}

    for key, value in dict1.items():
        if value in dict2:
            result[key] = dict2[value]
    return result


dict1 = {'a': 'p', 'b': 'r', 'c': 'g', 'd': 'p', 'e': 's'}
dict2 = {'p': '1', 'g': '2', 'r': '3', 's': '4'}

result = composite(dict1, dict2)
print(result)

# 3
from itertools import product as cartesian_product

def product(*sets):
    if not sets:
        return {()} 
    product_result = set(cartesian_product(*sets))

    return product_result


s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

result = product(s1, s2)
print(result)

result = product(s1, s2, s3)
print(result)

result = product(s1)
print(result)
