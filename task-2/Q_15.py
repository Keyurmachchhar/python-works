def printMarksheet(rollNo,studentName,sub1,sub2,sub3,total,percentage):
    # print(rollNo,studentName,sub1,sub2,sub3,total,percentage,sep="\n",end="\n")
    print("\nMarksheet :\nRoll No : %d\nStudent Name : %s\n1st Subject Marks : %d\n2nd Subject Marks : %d\n3rd Subject Marks : %d\nTotal : %d\nPercentage : %f"%(rollNo,studentName,sub1,sub2,sub3,total,percentage))

rollNo = int(input("Enter Roll No :"))
studentName = input("Enter Name : ")
sub1 = int(input("Enter Subject 1 marks : "))
sub2 = int(input("Enter Subject 2 marks : "))
sub3 = int(input("Enter Subject 3 marks : "))

total = sub1+sub2+sub3

percentage = total/3

printMarksheet(rollNo,studentName,sub1,sub2,sub3,total,percentage)