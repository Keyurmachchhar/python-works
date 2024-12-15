num_1=int(input("Enter 1st Number :"))
num_2=int(input("Enter 2nd Number :"))
num_3=int(input("Enter 3rd Number :"))

if(num_1>num_2):
    if(num_1>num_3):
        print(num_1," is gratest number",sep='')
    else:
        print(num_3," is gratest number",sep='')
else:
    if(num_2>num_3):
        print(num_2," is gratest number",sep='')
    else:
        print(num_3," is gratest number",sep='')