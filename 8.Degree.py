class Number:
    def __init__(self, number, degree):
        self.number = number
        self.degree = degree

    def exponentiation(self):
        return self.number ** self.degree


num = input()
deg = input()
a = Number(int(num), int(deg))

print(a.exponentiation())

input()
