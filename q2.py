# this is the answer cript for euler question 2


def fibonacci(end):
    first = 0
    second = 1
    total = 0
    while True:
        second, first = first + second, second
        if second > end:
            break
        else:
            if second%2 == 0:
                total += second
    return total


print(fibonacci(4000000))

