def sumDiff(firstVar, secondVar):
    amount = firstVar + secondVar
    diff = firstVar - secondVar
    result = [amount, diff]
    return result


def main():
    fV = input()
    sV = input()

    result = sumDiff(int(fV), int(sV))
    print(result)

    input()


if __name__ == "__main__":
    main()
