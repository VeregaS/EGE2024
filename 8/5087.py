from itertools import product

words = product('СТЕКЛО', repeat=5)

new_words = []
for word in words:
    word = ''.join(word)
    new_words.append(word)

new_words = sorted(new_words)

for word in new_words:
    if word[0] == 'С' and 'ОО' in word:
        print(new_words.index(word) + 1)
        break
