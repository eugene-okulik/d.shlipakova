def repeating(dictionary):
    for word, number in dictionary.items():
        print(word * number)

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

repeating(words)
