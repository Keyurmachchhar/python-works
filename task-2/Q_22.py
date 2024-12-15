num=int(input("Enter Number : "))

rev=0

while(num>0):
    mod=num%10
    rev=(rev*10)+mod
    num//=10

print(rev)