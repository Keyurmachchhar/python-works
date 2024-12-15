try:
    num = int(input("Enter Number : "))
except Exception:
    print("Exception raised")
else:
    print("You are in else statement")
finally:
    print("You are in finally statement")