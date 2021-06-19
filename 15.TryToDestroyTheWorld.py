def DivideByZero(_number):
    try:
        _number = _number / 0
    except ZeroDivisionError:
        print("Error! Attempt to divide by zero!!")


num = input()
DivideByZero(int(num))

input()
