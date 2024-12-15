try:
    num = int(input("Enter Number : "))

    if num < 1:
        raise ValueError
except ValueError:
    print("ValueError raised")
