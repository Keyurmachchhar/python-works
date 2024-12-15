num_1 = int(input("Enter 1st Number : "))
num_2 = int(input("Enter 2nd Number : "))

sum = lambda num1,num2:num1+num2

print("Addition of two numbers is %d"%sum(num_1,num_2))