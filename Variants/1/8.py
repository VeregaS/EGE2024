from itertools import product

words = sorted([''.join(i) for i in list(product('МАНГУСТ', repeat=6))])
indexes = []
for word in words:
    if word[0] != 'У':
        if word.count('М') == 2:
            if word.count('Г') <= 1:
                indexes.append(words.index(word) + 1)
print(max(indexes))