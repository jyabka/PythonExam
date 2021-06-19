def createList():
    c_list = []
    for i in range(0, 20):
        i = (i + 1) ** 3
        c_list.append(i)

    print(c_list)

    for i in range(0, 5):
        print(c_list[i])


createList()

input()
