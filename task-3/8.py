try:
    num = int(input("Enter Number : "))

    if(num < 1):
        raise Exception
except ValueError:
    print("You can not enter zero or negative number 1")
except Exception:
    print("You can not enter zero or negative number 2")