# Area of Circle

def AreaCircle(R):

    pi=3.14
    return pi*R*R

def main():
    Radius=int(input("Enter radius: "))

    Area=AreaCircle(Radius)

    print("Area of Circle is : ",Area )

if __name__=="__main__":
    main()