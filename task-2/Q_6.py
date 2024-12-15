while True:

    print("1. Contest\n2. IT\n3. Quiz\n4. Database\n5.Treasure Hunt\n6. Exit")
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        print("Contest is selected")
    elif choice==2:
        print("IT is selected")
    elif choice==3:
        print("Quiz is selected")
    elif choice==4:
        print("Database is selected")
    elif choice==5:
        print("Treasure Hunt is selected")
    elif choice==6:
        exit(0)
        break
    else:
        print("Invalid Choice")