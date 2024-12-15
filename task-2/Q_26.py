def keywordArgs(cel):
    print("%f celcius = %f fehrenheit"%(cel,(cel * (9/5))+32))

def defaultArgument(cel=0):
    print("%f celcius = %f fehrenheit"%(cel,(cel * (9/5))+32))

def returnArgument(cel):
    return (cel * (9/5))+32

fahrenheit = lambda cel=0:(cel * (9/5))+32

celcius = float(input("Enter Celcius : "))

print(keywordArgs(cel=celcius))
print(defaultArgument())
print("%f celcius = %f fehrenheit"%(celcius,returnArgument(celcius)))
print(fahrenheit(celcius))