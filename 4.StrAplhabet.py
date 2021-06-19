# Str Alphabet

alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

userString = input().casefold()

newString = ""

for word in userString:
    for index in alphabet:
        if word == index:
            print(word)

input()
