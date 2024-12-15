num_1 = int(input("Enter 1st Number : "))
num_2 = int(input("Enter 2nd number : "))

greatest = lambda num1=1,num2=0:num1 if(num1>num2) else num2

print(greatest(num_1,num_2)," is greatest",sep="")