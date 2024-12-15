num=int(input("Enter Number : "))

flag=False

for i in range(2,num):
    if(num%i==0):
        falg=False
        break
    else:
        flag=True

if(flag==True):
    print(num," is prime number",sep="")
else:
    print(num," is not prime number",sep="")