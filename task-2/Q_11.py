numbers=[]

evenCount=0
oddCount=0

for i in range(5):
    numbers.append(int(input("Enter Number :")))

for i in range(0,5):
    if(i%2==0):
        evenCount+=1
    else:
        oddCount+=1
    
print("Count of odd numbers : ",oddCount,sep="")
print("Count of even numbers : ",evenCount,sep="")