class Str:

    def __init__(self, c_string):
        self.c_string = c_string

    def user_input(self):
        self.c_string = input()
        return self.c_string

    def toUpperCase(self):
        print(self.c_string.upper())


c_str = Str("")

c_str.user_input()
c_str.toUpperCase()
