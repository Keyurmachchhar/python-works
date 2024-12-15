a=input("Please enter string:")

if(len(a)%2==0):
    fc=int((len(a)/2)-1)
    sc=int((len(a)/2)+1)
    print(a[fc:sc])
else:
    print(a[int(len(a)/2)])