alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
userString = input().casefold()

print(alphabet)

acc = []
for word in userString:
    for word_alphabet in range(ord('a'), ord('z')+1, 2):
        if word == chr(word_alphabet):
            if chr(word_alphabet) not in acc:
                acc.append(word)
                break
print(acc)

