# Print factors of given number

def Table(No):
    Sum=0

    for i in range(1,No+1):
        if No%i==0:
            Sum=Sum+i

    return Sum

def main():
    Value=int(input("Enter number: "))

    Ret=Table(Value)

    print("Addition of Factors of given number: ",Ret )

if __name__=="__main__":
    main()