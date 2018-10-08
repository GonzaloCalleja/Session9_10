
def test(number, odd=True):

    if odd:
        if number % 2 == 0:
            odd = False

    else:
        if number % 2 == 1:
            odd = False

    return odd


num = int(input("Please introduce a number: "))

if test(num):
    print("The number is odd.")
else:
    print("The number is even.")
