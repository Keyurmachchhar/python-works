numbers=[]

sum=0

for i in range(5):
    numbers.append(int(input("Enter Number :")))

for i in numbers:
    sum+=i
    
print("Sum : ",sum,sep="")