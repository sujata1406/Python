# Area of Rectangle

def RectangleArea(Len,Wid):
    return Len * Wid

def main():
    Length=int(input("Enter length: "))

    Width=int(input("Enter width: "))

    Area=RectangleArea(Length,Width)

    print("Area of Rectangle is : ",Area )

if __name__=="__main__":
    main()
