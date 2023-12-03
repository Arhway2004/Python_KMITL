def textese(s):
    # Define the dictionary of abbreviations with keys in lowercase
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
        "wait": "w8",  # Fix the key to be in lowercase
        "later": "i8r",  # Fix the key to be in lowercase
        "tomorrow": "2mro",
        "for": "4",
        "before": "b4",
        "once": "1ce",
        "and": "&",
        "your": "ur",  # Fix the key to be in lowercase
        "you're": "ur",  # Fix the key to be in lowercase
        "as far as i know": "afaik",  # Fix the key to be in lowercase
        "as soon as possible": "asap",  # Fix the key to be in lowercase
        "at the moment": "atm",  # Fix the key to be in lowercase
        "be right back": "brb",  # Fix the key to be in lowercase
        "by the way": "btw",  # Fix the key to be in lowercase
        "for your information": "fyi",  # Fix the key to be in lowercase
        "in my humble opinion": "imho",  # Fix the key to be in lowercase
        "in my opinion": "imo",  # Fix the key to be in lowercase
        "laughing out loud": "lol",  # Fix the key to be in lowercase
        "oh my god": "omg",  # Fix the key to be in lowercase
        "rolling on the floor laughing": "rofl",  # Fix the key to be in lowercase
        "talk to you later": "ttyl",  # Fix the key to be in lowercase
    }

    # Split the input string into words
    words = s.split()

    # Replace words with their abbreviations
    abbreviated_words = [abbreviations.get(word.lower(), word) for word in words]

    # Join the words to form the abbreviated message
    abbreviated_message = " ".join(abbreviated_words)

    return abbreviated_message

# Example usage:
message = "You're great"
result = textese(message)
print(result)
