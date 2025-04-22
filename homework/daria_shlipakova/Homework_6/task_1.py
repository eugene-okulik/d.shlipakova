text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

text = text.split()
new_text = []
for word in text:
    if word[-1] not in ',.':
        new_text.append(word + 'ing')
    else:
        new_text.append(word[:-1] + 'ing' + word[-1])
print(' '.join(new_text))
