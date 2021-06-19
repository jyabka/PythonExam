def comparison(first_string, second_string):
    if len(first_string) > len(second_string):
        print(first_string)
        return first_string
    elif len(first_string) < len(second_string):
        print(second_string)
        return second_string
    elif len(first_string) == len(second_string):
        print("Strings are equal in length")
        return


string_a = input()
string_b = input()

comparison(string_a, string_b)

input()
