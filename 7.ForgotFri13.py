a = [10, 13, 16, 4, 7, 13, 2, 13]
print(a)

for index in a:
    try:
        a.remove(13)
    except:
        break

print(a)

input()
