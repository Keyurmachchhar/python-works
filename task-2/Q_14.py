num=int(input("Enter Three Digit Number : "))

sum=0
temp=num

while(temp>0):
    mod=temp%10
    sum+=mod
    temp//=10

print(sum)