def perimeterOfSquare(length):
    return 4*length

def perimeterOfRectange(length,width):
    return 2*(length+width)


lengthOfSquare = float(input("Enter Length of Square : "))
print("Perimeter of square : ",perimeterOfSquare(lengthOfSquare),sep='')

lengthOfRectangle = float(input("\nEnter Length of rectangle : "))
widthOfRectangle = float(input("Enter Width of rectangle : "))
print("Perimeter of rectangle : ",perimeterOfRectange(lengthOfRectangle,widthOfRectangle),sep="")